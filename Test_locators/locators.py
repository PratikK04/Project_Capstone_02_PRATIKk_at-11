class Test_locators():
    #Login Locators
    username_locator = 'username'
    password_locator = 'password'
    login_button = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    # Validation Test Locators
    search_inputbox = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    PIM_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    Add_employee = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    search_button = '(//*[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"])'

    #Admin select Locator
    admin ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a' 
    user_management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    user = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li'
    userrole = '//*[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]'
    admin_select= "(//*[@role='listbox']//*[text()='Admin'])"
    Enable = "(//*[@role='listbox']//*[text()='Enabled'])"
    ESS_select ="(//*[@role='listbox']//*[text()='ESS'])"
    disable = "(//*[@role='listbox']//*[text()='general.disabled'])"

    #Input locators for adding employee
    Name_inputbox = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    lstname_inputbox = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    save_button = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    personal_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
    
    
    #PIM , creation of new user
    toggle_creat = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    ep_namebox = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    ep_mdnamebox = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    ep_lstnamebox = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    new_user = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    key_word ='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    cnf_password = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    cof_button = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    pers_details ='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    nick_name = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    dr_lic_loc = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    expiry_date = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    nationality =   "(//*[text()='Nationality']/parent::*/following-sibling::*/*/*)"
    indian = "(//*[@role='listbox']//*[text()='Indian'])"
    marital_status = "(//*[text()='Marital Status']/parent::*/following-sibling::*/*/*)"
    status_1 = "(//*[@role='listbox']//*[text()='Single'])"
    D0b_selector = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    Miltery= '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    Blood_group = "(//*[text()='Blood Type']/parent::*/following-sibling::*/*/*)"
    Blood_type ="(//*[@role='listbox']//*[text()='A+'])"
    save_btn1 = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    save_btn2 = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    edit_button = '(//*[@class="oxd-icon bi-pencil-fill"])'
    #PIM TC-06
    Contact_info = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
 
    contact_detail ='Contact Details'
    
    street_name01 ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    street_name02 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    
    city_loc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    
    state_loc = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    
    post_code = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    
    country_loc = "(//*[@class='oxd-select-text-input'])"
    
    drop_down = "//*[@role='listbox']"

    home = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    
    moblie = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    
    work = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    
    work_mail ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    
    other_mail = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    
    save_button2 = "(//*[@type='submit'])"

    #emergancy contact
    
    emergency_contact = 'Emergency Contacts'
    
    emergency_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
       
    name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    relationship = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    
    home_number =   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    
    mobile_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    
    work_no = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    
    save_button3 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    exit_dob ='(//*[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"])'

    #dependent Info
   
    Dependent = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
   
    Dependents_add = "(//*[@type='button'])[2]"
    
    Dependents_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    relationship_member = "(//*[@class='oxd-select-text-input'])"
    
    date_of_year = '(//*[@placeholder="yyyy-mm-dd"])'    
    
    ok_button = '(//*[@type="submit"])'

    #job Details
    
    job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a' 
    
    joined = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
   
    job_title = "(//*[@class='oxd-select-text-input'])[1]"
    
    job_category = "(//*[@class='oxd-select-text-input'])[2]"
    
    sub_unit = "(//*[@class='oxd-select-text-input'])[3]"
    
    location = "(//*[@class='oxd-select-text-input'])[4]"
    
    employee_status = "(//*[@class='oxd-select-text-input'])[5]"
    
    drop_down = "//*[@role='listbox']"

    #contrat termination locator
    

    a = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'

    contract_end_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'
    
    Yes_button = '(//*[@type="submit"])'
    
    Terminate = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    
    Terminate_employee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'

    Terminate_reason = "(//*[@class='oxd-select-text-input'])[6]"
    
    drop_down = "(//*[@role='listbox'])"
    
    note = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea'
        


    #Employee Activation locator

    save_button5 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'
    
    activate = '(//*[@type="button"])[2]'
    
    salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
     
    add_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    
    salary_component = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    
    pay_grade = "(//*[@class='oxd-select-text-input'])[1]"
    
    drop_down = "//*[@role='listbox']"



    #salary Details locator

    pay_frequency = "(//*[@class='oxd-select-text-input'])[2]"
    
    currency = "(//*[@class='oxd-select-text-input'])[3]"

    salary_amount = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    
    source_3 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    
    account = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    
    account_type = "(//*[@class='oxd-select-text-input'])[4]"

    routing = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    
    amount = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    
    save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'

    status_1= "(//*[@role='listbox']//*[text()='status 1'])"
    
    #tax details locator 
    
    Tax  = 'Tax Exemptions'
    
    federal_status = "(//*[@class='oxd-select-text-input'])[1]"
    
    drop_down = "//*[@role='listbox']"

    Exemptions = '(//*[@class="oxd-input oxd-input--active"])[2]'

    state_2 = "(//*[@class='oxd-select-text-input'])[2]"
    
    status_data = "(//*[@class='oxd-select-text-input'])[3]"
    
    
    tax_Exemptions = '(//*[@class="oxd-input oxd-input--active"])[3]'
    
    unemployee_state = "(//*[@class='oxd-select-text-input'])[4]"
    
    work_state = "(//*[@class='oxd-select-text-input'])[5]"
    
    complete = "(//*[@type='submit'])"
