class Variables:
    # script1
    menu = 'main-menu-item-text'
    menu_item = '//*[@id="__layout"]/div/header/div/div[1]/div/div/nav/ul/li[1]/div/div[1]/a[1]'
    special_word = 'special'
    search_icon = 'bama-small-search'
    search_input = 'globalSearchInput'
    result_one = '#__layout > div > div.bama-global-search.bama-global-search--active > ' \
                 'div.bama-global-search__result-container > div.bama-global-search__result-holder > a:nth-child(1) '
    # script2
    profile = "profile"
    auth_login = "auth-button"
    phone_number = "//*[contains(@id, 'phone')]"
    iFrame = "iframe#loginFrame"
    continue_button = "continue-button"
    otp_one = "txt-otp-1"
    otp_two = "txt-otp-2"
    otp_three = "txt-otp-3"
    otp_four = "txt-otp-4"

    # script3
    large_search_bar = "bama-large-search"
    search_result = "//*[@id='__layout']/div/div[2]/div[2]/div[2]/a[1]/span"

    # calculator
    cal_button = "//*[@id='__layout']/div/div[1]/div/div/div[2]/button"
    car_brand = "#__layout > div > div.main-wrapper > div > div > " \
                "div.calculator-brand-selector-section.calculator-step-item-comp > div > button:nth-child(7) "
    remove_brand = "#__layout > div > div.main-wrapper > div > div > div.calculator-side-bar > div > div > " \
                   "div.single-item.active-border > div.item-content-holder > div "

