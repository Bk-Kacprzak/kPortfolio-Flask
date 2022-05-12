from flask import redirect, url_for
from flask import request 

def redirect_to_next_page(default_url) : 
    _next = request.args.get('next') 
    if _next:
        if not is_safe_url(next): 
            return abort(400)
    return redirect(_next or url_for(default_url))



def url_for_other_page(**kwargs):
    """Returns a URL aimed at the current request endpoint and query args."""
    url_for_args = request.args.copy()
    if 'pjax' in url_for_args:
        url_for_args.pop('_pjax')
    for key, value in kwargs.items():
        url_for_args[key] = value
    return url_for(request.endpoint, **url_for_args)
