http_status = 200

match http_status:
    
    case 200|201:
        print("Succes")

    case 400:
        print("Bad Request")

    case 404:
        print("Not Found")

    case 500|501:
        print("Server Error")

    case _:
        print("Unknown")