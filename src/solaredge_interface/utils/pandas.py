
import re
import collections
import pandas as pd


def data_to_pandas(data, sep='.', prefix_to_remove=None):
    column_names, data_table = tabelize_data(
        data=flatten_data(data, sep=sep),
        sep=sep,
        prefix_remove=prefix_to_remove
    )
    return pd.DataFrame.from_dict(data_table, orient='index', columns=column_names)


def flatten_data(data, sep='.'):
    obj = collections.OrderedDict()

    def data_recurse(t, parent_key=''):
        if isinstance(t, list):
            for index in range(len(t)):
                data_recurse(t[index], parent_key + sep + str(index) if parent_key else str(index))
        elif isinstance(t, dict):
            for key, value in t.items():
                data_recurse(value, parent_key + sep + key if parent_key else key)
        else:
            obj[parent_key] = t

    data_recurse(data)
    return obj


def tabelize_data(data, sep='.', prefix_remove=None):

    def column_name_row_group(key_name):
        pattern_string = '\\{}'.format(sep) + '[0-9]+' + '\\{}'.format(sep)
        pattern = re.compile(pattern_string)
        matches = pattern.findall(key_name)
        column_index_key = ''
        if matches:
            for match in matches:
                key_name = key_name.replace(match, sep)
                column_index_key = '{}{}'.format(column_index_key, match.replace(sep,''))
        if prefix_remove and key_name.startswith(prefix_remove):
            return key_name[len(prefix_remove):], column_index_key
        return key_name, column_index_key

    # scan for column_names and row_groups
    column_names = []
    column_index_depth = 0
    for key, _ in data.items():
        column_name, row_group = column_name_row_group(key)
        if len(row_group) > column_index_depth:
            column_index_depth = len(row_group)
        if column_name not in column_names:
            column_names.append(column_name)

    # group data together in row_groups with column_names; maintain a row_group counter index
    data_group = collections.OrderedDict()
    row_group_index = 0
    row_group_index_map = collections.OrderedDict()
    for key, value in data.items():
        column_name, row_group_short = column_name_row_group(key)
        row_group = row_group_short.ljust(column_index_depth, '0')
        if row_group not in data_group.keys():
            data_group[row_group] = collections.OrderedDict()
            row_group_index_map[row_group] = row_group_index
            row_group_index += 1
        data_group[row_group][column_name] = value

    # map data into an ordered per row dict
    data_table = collections.OrderedDict()
    previous_group_index_key = '0' * column_index_depth
    for group_index_key, group_index_value in row_group_index_map.items():
        row_name = 'row_{}'.format(group_index_value)
        data_table[row_name] = []
        for column_name in column_names:
            if column_name not in data_group[group_index_key].keys():
                if column_name in data_group[previous_group_index_key].keys():
                    data_group[group_index_key][column_name] = data_group[previous_group_index_key][column_name]
                else:
                    data_group[group_index_key][column_name] = None
            data_table[row_name].append(data_group[group_index_key][column_name])
        previous_group_index_key = group_index_key

    return column_names, data_table
