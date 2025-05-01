def create_driver(browser="chrome"):
    try:
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        return driver
    except Exception as e:
        raise Exception(f"Error initializing WebDriver: {str(e)}")
