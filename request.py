from urllib import parse as url_parser

# call service
def get_address(self, request):
    query_params = url_parser.parse_qsl(url_parser.urlsplit(str(request.url)).query)
    client_list = [client for param_name, client in query_params if param_name == 'clients']
