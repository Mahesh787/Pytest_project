class Screen:
    def Screenshots(self, path,driver):
        self.driver = driver
        screenshot = self.driver.save_screenshot(path)
        return screenshot
