# Element Locators

sign_in = '''//div[@class="header_user_info"]/a[@class="login"]'''
email = '''//form[@id="login_form"]/div[@class="form_content clearfix"]/div[@class="form-group"]/input[@name="email"]'''
password = '''//form[@id="login_form"]/div[@class="form_content clearfix"]/div[@class="form-group"]/span/input[@name="passwd"]'''
submit = '''//div[@class="form_content clearfix"]/p[@class="submit"]/button[@type="submit"]'''

# signup locators
signup_email = '''.//form[@id="create-account_form"]/div[@class="form_content clearfix"]/div[@class="form-group"]/input'''
#signup_submit ='''.//form[@id="create-account_form"]/div[@class="form_content clearfix"]/div[@class="submit"]'''
signup_submit ='''.//form[@id="create-account_form"]/div[@class="form_content clearfix"]/div[@class="submit"]/button[@id="SubmitCreate"]'''
signup_error = '''.//div[@class="alert alert-danger"]/ol/li'''
signup_gender_male = '''.//div[@class="radio-inline"]/label/div/span/input[@id="id_gender1"]'''
signup_first_name = '''.//div[@class="required form-group"]/input[@id="customer_firstname"]'''
signup_last_name = '''.//div[@class="required form-group"]/input[@id="customer_lastname"]'''
signup_pwd = '''.//div[@class="required password form-group"]/input[@id="passwd"]'''
signup_days = '''.//div[@class="col-xs-4"]/div/select[@id="days"]'''
signup_months = '''.//div[@class="col-xs-4"]/div/select[@id="months"]'''
signup_years = '''.//div[@class="col-xs-4"]/div/select[@id="years"]'''
signup_address = '''.//div[@class="account_creation"]/p/input[@id="address1"]'''
signup_city = '''.//div[@class="account_creation"]/p/input[@name="city"]'''
signup_state = '''.//div[@class="account_creation"]/p/div/select[@name="id_state"]'''
signup_zipcode = '''.//div[@class="account_creation"]/p/input[@name="postcode"]'''
signup_country = '''.//div[@class="account_creation"]/p/div/select[@name="id_country"]'''
signup_mobile = '''.//div[@class="account_creation"]/p/input[@name="phone_mobile"]'''
signup_alis = '''.//div[@class="account_creation"]/p/input[@name="alias"]'''
signup_register = '''.//div[@class="submit clearfix"]/button'''

login_error ='''.//div[@class="alert alert-danger"]/ol/li'''



