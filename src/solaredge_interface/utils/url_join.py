

def url_join(*parts):
    """
    Join terms together with forward slashes
    """

    # first strip extra forward slashes (except http:// and the likes) and
    # create list
    part_list = []
    for part in parts:
        p = str(part)
        if p.endswith('//'):
            p = p[0:-1]
        else:
            p = p.strip('/')
        part_list.append(p)

    # join everything together
    url = '/'.join(part_list)
    return url


def url_join_site_ids(data):

    if type(data) is list:
        return url_join('sites', ','.join(data).replace(' ',''))
    elif ',' in str(data):
        return url_join('sites', data.replace(' ',''))
    else:
        return url_join('site', data.replace(' ',''))
