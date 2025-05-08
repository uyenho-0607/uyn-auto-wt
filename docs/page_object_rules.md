# Page Object Writing Rules

## File Structure

Page object files should follow this structure:
```python
class PageName(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    # Locator definitions

    # ------------------------ ACTIONS ------------------------ #
    # Action methods

    # ------------------------ VERIFY ------------------------ #
    # Verification methods
```

## Sections

### 1. Locators
- Use private variables with double underscore prefix
- Use descriptive names
- Group related locators together
- Use data-testid attributes when available

Example:
```python
# ------------------------ LOCATORS ------------------------ #
__txt_user_id = (By.CSS_SELECTOR, "input[data-testid='login-user-id']")
__txt_password = (By.CSS_SELECTOR, "input[data-testid='login-password']")
__btn_login = (By.CSS_SELECTOR, "button[data-testid='login-submit']")
__tab_account_type = (By.CSS_SELECTOR, "*[data-testid='tab-login-account-type-{}']")
```

### 2. Actions
- Methods should be public
- Use descriptive method names
- Include type hints
- Handle dynamic locators using `cook_element`

Example:
```python
# ------------------------ ACTIONS ------------------------ #
def select_language(self, language: Language):
    self.actions.click(self.__drp_language)
    self.actions.click(cook_element(self.__opt_language, language))

def login(self, userid, password, account_type: AccountType, language: Language = None):
    if language:
        self.select_language(language)

    self.actions.click(cook_element(self.__tab_account_type, account_type.lower()))
    self.actions.send_keys(self.__txt_user_id, str(userid))
    self.actions.send_keys(self.__txt_password, str(password))
    self.actions.click(self.__btn_login)
```

### 3. Verifications
- Methods should be public
- Use descriptive method names
- Include clear assertion messages
- Use soft assertions

Example:

```python
# ------------------------ VERIFY ------------------------ #
def verify_alert_error_message(self):
    """Verify that the alert error message is displayed with correct text"""
    actual_err = self.actions.get_text(self.__alert_error)
    soft_assert(actual_err, UIMessages.AlertError.INVALID_CREDENTIALS, "Error message validation failed!")


def verify_login_failed(self):
    """Verify login failure by checking login page URL and error message"""
    self.verify_page_url(URLPaths.LOGIN)
    self.verify_message()
```

## Best Practices

1. **Locator Management**
   - Use data-testid attributes for stable locators
   - Keep locators private
   - Use meaningful names
   - Document complex locators
   - Group related locators
   - Use appropriate locator strategies
   - Avoid XPath when possible
   - Keep locators maintainable

2. **Action Methods**
   - Keep methods focused and single-purpose
   - Use type hints
   - Handle optional parameters
   - Convert parameters to strings when needed
   - Use meaningful method names
   - Document complex actions
   - Handle exceptions appropriately
   - Return appropriate values

3. **Verification Methods**
   - Include clear assertion messages
   - Use soft assertions for multiple checks
   - Document verification logic
   - Handle expected states
   - Verify one thing per method
   - Use appropriate wait strategies
   - Handle dynamic content
   - Include timeout parameters

4. **Code Organization**
   - Group related methods together
   - Use clear section comments
   - Follow consistent naming conventions
   - Inherit from BasePage
   - Keep methods small and focused
   - Use appropriate access modifiers
   - Follow SOLID principles
   - Maintain clean architecture

5. **Error Handling**
   - Include verification methods for error states
   - Handle dynamic elements
   - Document expected behaviors
   - Use appropriate exception handling
   - Provide meaningful error messages
   - Handle edge cases
   - Implement retry mechanisms
   - Log errors appropriately

6. **Performance**
   - Optimize locator strategies
   - Minimize unnecessary waits
   - Use efficient selectors
   - Cache elements when appropriate
   - Handle dynamic content efficiently
   - Implement proper wait strategies
   - Avoid redundant operations
   - Optimize method calls

7. **Maintainability**
   - Keep code DRY (Don't Repeat Yourself)
   - Use inheritance effectively
   - Document complex logic
   - Follow consistent patterns
   - Use meaningful names
   - Keep methods small
   - Use appropriate comments
   - Regular code review

8. **Testing**
   - Write unit tests for page objects
   - Test edge cases
   - Verify error handling
   - Test dynamic content
   - Validate locators
   - Test parameter handling
   - Verify timeout behavior
   - Test retry mechanisms

## Code Quality Examples

### Good Page Object
```python
class LoginPage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __txt_user_id = (By.CSS_SELECTOR, "input[data-testid='login-user-id']")
    __txt_password = (By.CSS_SELECTOR, "input[data-testid='login-password']")
    __btn_login = (By.CSS_SELECTOR, "button[data-testid='login-submit']")

    # ------------------------ ACTIONS ------------------------ #
    def login(self, username: str, password: str, account_type: AccountType, language: Language = None) -> None:
        """
        Perform login action with given credentials
        
        Args:
            username: User ID for login
            password: Password for login
            account_type: Type of account (DEMO/LIVE)
            language: Optional language selection
        """
        if language:
            self.select_language(language)

        self.actions.click(cook_element(self.__tab_account_type, account_type.lower()))
        self.actions.send_keys(self.__txt_user_id, str(username))
        self.actions.send_keys(self.__txt_password, str(password))
        self.actions.click(self.__btn_login)

    # ------------------------ VERIFY ------------------------ #
    def verify_login_successful(self, expected_url: str) -> None:
        """
        Verify successful login by checking URL and account tab
        
        Args:
            expected_url: Expected URL after successful login
        """
        self.verify_page_url(expected_url)
        self.verify_account_tab_is_displayed()
```

### Bad Page Object (Avoid)
```python
class LoginPage:
    # Bad: Public locators
    user_id = (By.CSS_SELECTOR, "input#user")
    password = (By.CSS_SELECTOR, "input#pass")
    
    # Bad: No type hints, no documentation
    def login(self, user, pass, type):
        self.driver.find_element(*self.user_id).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pass)
        self.driver.find_element(By.CSS_SELECTOR, f"button[type='{type}']").click()
    
    # Bad: No error handling, no assertions
    def verify_login(self):
        return self.driver.current_url == "/trade"
```

## Page Object Checklist

Before submitting a page object, ensure:
- [ ] All locators are private and well-named
- [ ] Methods have proper type hints
- [ ] Complex methods are documented
- [ ] Error handling is implemented
- [ ] Verification methods are clear
- [ ] Code follows style guide
- [ ] No duplicate code
- [ ] Proper inheritance is used
- [ ] Performance is considered
- [ ] Tests are written

## Example Page Object

```python
from selenium.webdriver.common.by import By
from src.core.actions.web_actions import WebActions
from src.data.enums import AccountType, Language, URLPaths
from src.data.ui_messages import UIMessages
from src.page_object.web.base_page import BasePage
from src.utils.assert_utils import soft_assert
from src.utils.common_utils import cook_element


class LoginPage(BasePage):
   def __init__(self, actions: WebActions):
      super().__init__(actions)

   # ------------------------ LOCATORS ------------------------ #
   __txt_user_id = (By.CSS_SELECTOR, "input[data-testid='login-user-id']")
   __txt_password = (By.CSS_SELECTOR, "input[data-testid='login-password']")
   __btn_login = (By.CSS_SELECTOR, "button[data-testid='login-submit']")
   __tab_account_type = (By.CSS_SELECTOR, "*[data-testid='tab-login-account-type-{}']")
   __drp_language = (By.CSS_SELECTOR, "*[data-testid='language-dropdown']")
   __opt_language = (By.XPATH, "//li[@data-testid='language-option' and text()='{}']")
   __alert_error = (By.CSS_SELECTOR, "*[data-testid='alert-error']")

   # ------------------------ ACTIONS ------------------------ #
   def select_language(self, language: Language):
      self.actions.click(self.__drp_language)
      self.actions.click(cook_element(self.__opt_language, language))

   def login(self, userid, password, account_type: AccountType, language: Language = None):
      if language:
         self.select_language(language)

      self.actions.click(cook_element(self.__tab_account_type, account_type.lower()))
      self.actions.send_keys(self.__txt_user_id, str(userid))
      self.actions.send_keys(self.__txt_password, str(password))
      self.actions.click(self.__btn_login)

   # ------------------------ VERIFY ------------------------ #
   def verify_alert_error_message(self):
      """Verify that the alert error message is displayed with correct text"""
      actual_err = self.actions.get_text(self.__alert_error)
      soft_assert(actual_err, UIMessages.AlertError.INVALID_CREDENTIALS, "Error message validation failed!")

   def verify_login_failed(self):
      """Verify login failure by checking login page URL and error message"""
      self.verify_page_url(URLPaths.LOGIN)
      self.verify_alert_error_message()
``` 