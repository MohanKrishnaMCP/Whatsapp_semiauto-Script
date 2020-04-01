from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'D:/Programs/chrome driver/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

print("---------------Whatsapp semiauto message-----------------")

while True:
	name = []
	no_users = int(input('Enter the number of receivers: '))

	for i in range(no_users):
		u_name = str(input('Enter the name: '))
		name.append(u_name)

	print(name)
	msg = input('Enter the message: ')
	count = int(input('Enter the count: '))

	input('Enter anything after scanning')

	for receiver in name:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(receiver))
		user.click()

		msg_box = driver.find_element_by_class_name('_3FeAD')

		for i in range(count):
			msg_box.send_keys(msg)
			button = driver.find_element_by_class_name('_3M-N-')
			button.click()
