#1.Scroll down pag by pixel

#driver.execute_script("window.scrollBy(0,3000)","")
#driver.execute_script("return window.pageYOffset;")

#2.Scroll down page till element is visible

#flag=driver.findelement()
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#driver.execute_script("return window.pageYOffset;")

#3.Scroll down page till end
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#driver.execute_script("return window.pageYOffset;")

#4.Scroll up to starting position
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#driver.execute_script("return window.pageYOffset;")