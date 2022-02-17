if __name__ == '__main__':
    from module.browser_mng import browserManage
    driver = browserManage().get_driver()
    driver.get('https://kojinjigyou.org/')
    login_link = driver.find_element_by_link_text('ログイン')
    login_link.click()
    import json
    login_setting = json.load(open('settings/blog_login_setting.json', 'r'))
    login_id = driver.find_element_by_id('user_login')
    login_id.send_keys(login_setting['login_user'])
    login_id = driver.find_element_by_id('user_pass')
    login_id.send_keys(login_setting['login_password'])
    login_id = driver.find_element_by_id('user_pass')
    login_submit_link = driver.find_element_by_id('wp-submit')
    login_submit_link.click()
    
    driver.quit()