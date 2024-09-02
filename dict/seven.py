users=[{'eid':1,'ename':'Nixie','email':'nmacquist0@walmart.com','gender':'Female'},
{'eid':2,'ename':'Joyce','email':'jnoell1@earthlink.net','gender':'Female'},
{'eid':3,'ename':'Barron','email':'bmccullen2@senate.gov','gender':'Male'},
{'eid':4,'ename':'Claudie','email':'cwale3@reverbnation.com','gender':'Female'},
{'eid':5,'ename':'Damiano','email':'dbourley4@cdbaby.com','gender':'Non-binary'},
{'eid':6,'ename':'Maxi','email':'mmanuely5@miitbeian.gov.cn','gender':'Female'},
{'eid':7,'ename':'Augusta','email':'ahanham6@163.com','gender':'Female'},
{'eid':8,'ename':'Trixy','email':'tstockney7@examiner.com','gender':'Female'},
{'eid':9,'ename':'Karalee','email':'kimpson8@amazon.co.uk','gender':'Female'},
{'eid':10,'ename':'Jodee','email':'jpresidey9@sohu.com','gender':'Female'},
{'eid':11,'ename':'Johnath','email':'jpaintera@telegraph.co.uk','gender':'Female'},
{'eid':12,'ename':'Delmer','email':'dgeppb@bloglovin.com','gender':'Male'},
{'eid':13,'ename':'Penny','email':'pcollenc@nba.com','gender':'Male'},
{'eid':14,'ename':'Regina','email':'rtunnockd@squidoo.com','gender':'Genderqueer'},
{'eid':15,'ename':'Vanni','email':'vhaslocke@cocolog-nifty.com','gender':'Female'},
{'eid':16,'ename':'Salomone','email':'slabordef@behance.net','gender':'Male'},
{'eid':17,'ename':'Ailene','email':'akobschg@tiny.cc','gender':'Genderfluid'},
{'eid':18,'ename':'Dane','email':'drappah@cnn.com','gender':'Male'},
{'eid':19,'ename':'Marietta','email':'mkinetoni@alibaba.com','gender':'Female'},
{'eid':20,'ename':'Becky','email':'blowethj@google.de','gender':'Non-binary'},
{'eid':21,'ename':'Aldwin','email':'acanonk@google.co.jp','gender':'Male'},
{'eid':22,'ename':'Claiborn','email':'crhymerl@ow.ly','gender':'Male'},
{'eid':23,'ename':'Isa','email':'iberndtssenm@yahoo.com','gender':'Male'},
{'eid':24,'ename':'Pooh','email':'pwittmann@google.co.jp','gender':'Male'},
{'eid':25,'ename':'Arielle','email':'apinchino@163.com','gender':'Genderfluid'},
{'eid':26,'ename':'Gerry','email':'gtiltp@diigo.com','gender':'Male'},
{'eid':27,'ename':'Richmound','email':'rkilgroveq@howstuffworks.com','gender':'Male'},
{'eid':28,'ename':'Vinnie','email':'vgrigoreyr@furl.net','gender':'Male'},
{'eid':29,'ename':'Barret','email':'blimpertzs@dmoz.org','gender':'Male'},
{'eid':30,'ename':'Matthias','email':'mmacshirriet@cafepress.com','gender':'Male'},
{'eid':31,'ename':'Carlotta','email':'cfalkousu@cdc.gov','gender':'Female'},
{'eid':32,'ename':'Lyell','email':'lcasemorev@goodreads.com','gender':'Male'},
{'eid':33,'ename':'Chester','email':'ctiesw@mapy.cz','gender':'Male'},
{'eid':34,'ename':'Sanson','email':'schristianx@stanford.edu','gender':'Male'},
{'eid':35,'ename':'Rancell','email':'rgaynesfordy@skyrock.com','gender':'Male'},
{'eid':36,'ename':'Gerek','email':'gbrozekz@paypal.com','gender':'Male'},
{'eid':37,'ename':'Waverley','email':'wfairest10@myspace.com','gender':'Male'},
{'eid':38,'ename':'Valene','email':'vitzig11@histats.com','gender':'Female'},
{'eid':39,'ename':'Jeannette','email':'jsaipy12@ycombinator.com','gender':'Female'},
{'eid':40,'ename':'Larry','email':'lredwin13@ftc.gov','gender':'Genderqueer'},
{'eid':41,'ename':'Sherwynd','email':'sartrick14@ca.gov','gender':'Male'},
{'eid':42,'ename':'June','email':'jwinning15@list-manage.com','gender':'Genderqueer'},
{'eid':43,'ename':'Hi','email':'hcorrado16@symantec.com','gender':'Male'},
{'eid':44,'ename':'Virgie','email':'vmaunsell17@odnoklassniki.ru','gender':'Male'},
{'eid':45,'ename':'Rosamond','email':'rschwaiger18@shinystat.com','gender':'Genderqueer'},
{'eid':46,'ename':'Elaina','email':'esertin19@histats.com','gender':'Female'},
{'eid':47,'ename':'Mable','email':'mgai1a@blog.com','gender':'Female'},
{'eid':48,'ename':'Wash','email':'wklisch1b@wufoo.com','gender':'Male'},
{'eid':49,'ename':'Herman','email':'hwilgar1c@aol.com','gender':'Non-binary'},
{'eid':50,'ename':'Dee dee','email':'dcooke1d@nationalgeographic.com','gender':'Female'}
]



print(type(users))
male_users=0
female_users=0
for user in users:
    if user['gender']=='Male':
        male_users=male_users+1
    elif user['gender']=='Female':
        female_users=female_users+1
print(male_users)
print(female_users)