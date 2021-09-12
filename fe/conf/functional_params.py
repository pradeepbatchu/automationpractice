# Url
URL = "http://automationpractice.com/index.php"
UAT_URL = "http://automationpractice.com/index.php"


def get_base_url(environment):
    if environment == "qa":
        base_url = URL
    elif environment == "uat":
        base_url = UAT_URL
    else:
        raise ValueError('Unknown Environment: {} please try with: qa or uat'.format(environment))
    return base_url
