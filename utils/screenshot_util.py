import os
from datetime import datetime

def take_screenshot(driver,name='screenshot'):

    folder='screenshots'
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp=datetime.now().strftime('%Y%m%d_%H%M')
    filepath=f'{folder}/{name}_{timestamp}.png'
    driver.save_screenshot(filepath)
    print(f'>>>>>> Screenshot saved to {filepath}')
    return filepath