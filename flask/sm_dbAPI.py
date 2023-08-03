## CS 3308 Group Project
## Team 2: Space Monkeys
## Main database driver code
## Last Update: Travis Byrne, 2 August 2023

import sqlite3
import datetime

# Creates a database with the filename given. Create the required tables and fields.
def create(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''CREATE TABLE Bloodbanks_and_Hospitals
                (Institution_ID INT, 
                Type VARCHAR(45), 
                Name VARCHAR(90), 
                City VARCHAR(45), 
                State VARCHAR(2), 
                A_Positive_Units INT, 
                A_Negative_Units INT, 
                B_Positive_Units INT,
                B_Negative_Units INT,
                AB_Positive_Units INT,
                AB_Negative_Units INT,
                O_Positive_Units INT,
                O_Negative_Units INT,
                PRIMARY KEY(Institution_ID));''')
    c.execute('''CREATE TABLE Donor
                (Donor_ID INT, 
                Name VARCHAR(90), 
                Blood_Type VARCHAR(3), 
                PRIMARY KEY(Donor_ID));''')
    c.execute('''CREATE TABLE Patient
                (Patient_ID INT, 
                Name VARCHAR(90), 
                Blood_Type VARCHAR(3), 
                PRIMARY KEY(Patient_ID));''')
    c.execute('''CREATE TABLE Donation
                (Donation_ID INT, 
                Date_Time DATETIME, 
                Donor_ID INT, 
                Medical_Professional VARCHAR(90), 
                Hospital_ID INT, 
                Amount INT,
                PRIMARY KEY(Donation_ID),
                FOREIGN KEY(Donor_ID) REFERENCES Donor(Donor_ID),
                FOREIGN KEY(Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID));''')
    c.execute('''CREATE TABLE Transfusion
                (Transfusion_ID INT, 
                Date_Time DATETIME, 
                Donation_ID INT, 
                Patient_ID INT, 
                Medical_Professional VARCHAR(90), 
                Hospital_ID INT, 
                Amount INT,
                PRIMARY KEY(Transfusion_ID),
                FOREIGN KEY(Donation_ID) REFERENCES Donation(Donation_ID),
                FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID),
                FOREIGN KEY(Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID));''')
    c.execute('''CREATE TABLE Transfer
                (Transfer_ID INT, 
                Date_Time DATETIME,
                Donation_ID INT, 
                Receiving_Hospital_ID INT,
                Sending_Hospital_ID INT,
                PRIMARY KEY(Transfer_ID),
                FOREIGN KEY(Donation_ID) REFERENCES Donation(Donation_ID),
                FOREIGN KEY(Sending_Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID),
                FOREIGN KEY(Receiving_Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID));''')
    c.execute('''CREATE TABLE Complication
                (Complication_ID INT, 
                Transfusion_ID INT,
                Comments VARCHAR(180), 
                PRIMARY KEY(Complication_ID),
                FOREIGN KEY(Transfusion_ID) REFERENCES Transfusion(Transfusion_ID));''')
    conn.commit()
    conn.close()

def fill(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Fill in the Bloodbanks_and_Hospitals table
    Bloodbank_and_Hospital_insert = [(1, 'Hospital', 'Adams County', 'Brighton', 'CO', 10500, 1853, 18250, 3221, 1000, 7300, 80300, 14171),
        (2, 'Hospital', 'Alamosa County', 'Alamosa', 'CO', 11550, 2038, 18000, 3176, 1100, 7200, 79200, 13976),
        (3, 'Hospital', 'Arapahoe County', 'Littleton', 'CO', 12600, 2224, 17750, 3132, 1200, 7100, 78100, 13782),
        (4, 'Hospital', 'Archuleta County', 'Pagosa Springs', 'CO', 13650, 2409, 17500, 3088, 1300, 7000, 77000, 13588),
        (5, 'Hospital', 'Baca County', 'Springfield', 'CO', 14700, 2594, 17250, 3044, 1400, 6900, 75900, 13394),
        (6, 'Hospital', 'Bent County', 'Las Animas', 'CO', 15750, 2779, 17000, 3000, 1500, 6800, 74800, 13200),
        (7, 'Hospital', 'Boulder County', 'Boulder', 'CO', 16800, 2965, 16750, 2956, 1600, 6700, 73700, 13006),
        (8, 'Hospital', 'Broomfield County', 'Broomfield', 'CO', 17850, 3150, 16500, 2912, 1700, 6600, 72600, 12812),
        (9, 'Hospital', 'Chaffee County', 'Salida', 'CO', 18900, 3335, 16250, 2868, 1800, 6500, 71500, 12618),
        (10, 'Hospital', 'Cheyenne County', 'Cheyenne Wells', 'CO', 19950, 3521, 16000, 2824, 1900, 6400, 70400, 12424),
        (11, 'Hospital', 'Clear Creek County', 'Georgetown', 'CO', 21000, 3706, 15750, 2779, 2000, 6300, 69300, 12229),
        (12, 'Hospital', 'Conejos County', 'Conejos', 'CO', 22050, 3891, 15500, 2735, 2100, 6200, 68200, 12035),
        (13, 'Hospital', 'Costilla County', 'San Luis', 'CO', 23100, 4076, 15250, 2691, 2200, 6100, 67100, 11841),
        (14, 'Hospital', 'Crowley County', 'Ordway', 'CO', 24150, 4262, 15000, 2647, 2300, 6000, 66000, 11647),
        (15, 'Hospital', 'Custer County', 'Westcliffe', 'CO', 25200, 4447, 14750, 2603, 2400, 5900, 64900, 11453),
        (16, 'Hospital', 'Delta County', 'Delta', 'CO', 26250, 4632, 14500, 2559, 2500, 5800, 63800, 11259),
        (17, 'Hospital', 'Denver County', 'Denver', 'CO', 27300, 4818, 14250, 2515, 2600, 5700, 62700, 11065),
        (18, 'Hospital', 'Dolores County', 'Dove Creek', 'CO', 28350, 5003, 14000, 2471, 2700, 5600, 61600, 10871),
        (19, 'Hospital', 'Douglas County', 'Castle Rock', 'CO', 29400, 5188, 13750, 2426, 2800, 5500, 60500, 10676),
        (20, 'Hospital', 'Eagle County', 'Eagle', 'CO', 30450, 5374, 13500, 2382, 2900, 5400, 59400, 10482),
        (21, 'Hospital', 'El Paso County', 'Colorado Springs', 'CO', 31500, 5559, 13250, 2338, 3000, 5300, 58300, 10288),
        (22, 'Hospital', 'Elbert County', 'Kiowa', 'CO', 32550, 5744, 13000, 2294, 3100, 5200, 57200, 10094),
        (23, 'Hospital', 'Fremont County', 'Canon City', 'CO', 33600, 5929, 12750, 2250, 3200, 5100, 56100, 9900),
        (24, 'Hospital', 'Garfield County', 'Glenwood City', 'CO', 34650, 6115, 12500, 2206, 3300, 5000, 55000, 9706),
        (25, 'Hospital', 'Gilpin County', 'Central City', 'CO', 35700, 6300, 12250, 2162, 3400, 4900, 53900, 9512),
        (26, 'Hospital', 'Grand County', 'Hot Sulphur Springs', 'CO', 36750, 6485, 12000, 2118, 3500, 4800, 52800, 9318),
        (27, 'Hospital', 'Gunnison County', 'Gunnison', 'CO', 37800, 6671, 11750, 2074, 3600, 4700, 51700, 9124),
        (28, 'Hospital', 'Hinsdale County', 'Lake City', 'CO', 38850, 6856, 11500, 2029, 3700, 4600, 50600, 8929),
        (29, 'Hospital', 'Huerfano County', 'Walsenburg', 'CO', 39900, 7041, 11250, 1985, 3800, 4500, 49500, 8735),
        (30, 'Hospital', 'Jackson County', 'Walden', 'CO', 40950, 7226,11000, 1941, 3900, 4400, 48400, 8541),
        (31, 'Hospital', 'Jefferson County', 'Golden', 'CO', 42000, 7412, 10750, 1897, 4000, 4300, 47300, 8347),
        (32, 'Hospital', 'Kiowa County', 'Eads', 'CO', 43050, 7597, 10500, 1853, 4100, 4200, 46200, 8153),
        (33, 'Hospital', 'Kit Carson County', 'Burlington', 'CO', 44100, 7782, 10250, 1809, 4200, 4100, 45100, 7959),
        (34, 'Hospital', 'La Plata County', 'Durango', 'CO', 45150, 7968, 10000, 1765, 4300, 4000, 44000, 7765),
        (35, 'Hospital', 'Lake County', 'Leadville', 'CO', 46200, 8153, 9750, 1721, 4400, 3900, 42900, 7571),
        (36, 'Hospital', 'Larimer County', 'Fort Collins', 'CO', 47250, 8338, 9500, 1676, 4500, 3800, 41800, 7376),
        (37, 'Hospital', 'Las Animas County', 'Trinidad', 'CO', 48300, 8524,9250, 1632, 4600, 3700, 40700, 7182),
        (38, 'Hospital', 'Lincoln County', 'Hugo', 'CO', 49350, 8709, 9000, 1588, 4700, 3600, 39600, 6988),
        (39, 'Hospital', 'Logan County', 'Sterling', 'CO', 50400, 8894, 8750, 1544, 4800, 3500, 38500, 6794),
        (40, 'Hospital', 'Mesa County', 'Grand Junction', 'CO', 51450, 9079, 8500, 1500, 4900, 3400, 37400, 6600),
        (41, 'Hospital', 'Mineral County', 'Creede', 'CO', 52500, 9265, 8250, 1456, 5000, 3300, 36300, 6406),
        (42, 'Hospital', 'Moffat County', 'Craig', 'CO', 53550, 9450, 8000, 1412, 5100, 3200, 35200, 6212),
        (43, 'Hospital', 'Montezuma County', 'Cortez', 'CO', 54600, 9635, 7750, 1368, 5200, 3100, 34100, 6018),
        (44, 'Hospital', 'Montrose County', 'Montrose', 'CO', 55650, 9821, 7500, 1324, 5300, 3000, 33000, 5824),
        (45, 'Hospital', 'Morgan County', 'Fort Morgan', 'CO', 56700, 10006, 250, 1279, 5400, 2900, 31900, 5629),
        (46, 'Hospital', 'Otero County', 'La Junta', 'CO', 57750, 10191, 7000, 1235, 5500, 2800, 30800, 5435),
        (47, 'Hospital', 'Ouray County', 'Ouray', 'CO', 58800, 10376, 6750, 1191, 5600, 2700, 29700, 5241),
        (48, 'Hospital', 'Park County', 'Fairplay', 'CO', 59850, 10562, 6500, 1147, 5700, 2600, 28600, 5047),
        (49, 'Hospital', 'Phillips County', 'Holyoke', 'CO', 60900, 10747, 6250, 1103, 5800, 2500, 27500, 4853),
        (50, 'Hospital', 'Pitkin County', 'Aspen', 'CO', 61950, 10932, 6000, 1059, 5900, 2400, 26400, 4659),
        (51, 'Hospital', 'Prowers County', 'Lamar', 'CO', 63000, 11118, 5750, 1015, 6000, 2300, 25300, 4465),
        (52, 'Hospital', 'Pueblo County', 'Pueblo', 'CO', 64050, 11303, 5500, 971, 6100, 2200, 24200, 4271),
        (53, 'Hospital', 'Rio Blanco County', 'Meeker', 'CO', 65100, 11488, 5250, 926, 6200, 2100, 23100, 4076),
        (54, 'Hospital', 'Rio Grande County', 'Del Norte', 'CO', 66150, 11674, 5000, 882, 6300, 2000, 22000, 3882),
        (55, 'Hospital', 'Routt County', 'Steamboat Springs', 'CO', 67200, 11859, 4750, 838, 6400, 1900, 20900, 3688),
        (56, 'Hospital', 'Saguache County', 'Saguache', 'CO', 68250, 12044, 4500, 794, 6500, 1800, 19800, 3494),
        (57, 'Hospital', 'San Juan County', 'Silverton', 'CO', 69300, 12229, 4250, 750, 6600, 1700, 18700, 3300),
        (58, 'Hospital', 'San Miguel County', 'Telluride', 'CO', 70350, 12415, 4000, 706, 6700, 1600, 17600, 3106),
        (59, 'Hospital', 'Sedgwick County', 'Julesburg', 'CO', 71400, 12600, 3750, 662, 6800, 1500, 16500, 2912),
        (60, 'Hospital', 'Summit County', 'Breckenridge', 'CO', 72450, 12785, 3500, 618, 6900, 1400, 15400, 2718),
        (61, 'Hospital', 'Teller County', 'Cripple Creek', 'CO', 73500, 12971, 3250, 574, 7000, 1300, 14300, 2524),
        (62, 'Hospital', 'Washington County', 'Akron', 'CO', 74550, 13156, 3000, 529, 7100, 1200, 13200, 2329),
        (63, 'Hospital', 'Weld County', 'Greeley', 'CO', 75600, 13341, 2750, 485, 7200, 1100, 12100, 2135),
        (64, 'Hospital', 'Yuma County', 'Wray', 'CO', 76650, 13526, 2500, 441, 7300, 1000, 11000, 1941)]
    for (idhosp, banktype, name, city, state, ap, an, bp, bn, abp, abn, op, on) in Bloodbank_and_Hospital_insert:
        c.execute('''INSERT INTO Bloodbanks_and_Hospitals VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);''', (idhosp, banktype, name, city, state, ap, an, bp, bn, abp, abn, op, on))
        
    # Fill in the Donor table
    donor_insert = [(1, 'Bugs Bunny', 'A+'),
                    (2, 'Daffy Duck', 'A+'),
                    (3, 'Porky Pig', 'A+'),
                    (4, 'Elmer Fudd', 'A+'),
                    (5, 'Tweety Bird', 'A+'),
                    (6, 'Yosemite Sam', 'O+'),
                    (7, 'Lola Bunny', 'O+'),
                    (8, 'Snow White', 'O+'),
                    (9, 'Tinker Bell', 'O+'),
                    (10, 'Cinderlla Castle', 'O+'),
                    (11, 'Ariel Mermaid', 'A-'),
                    (12, 'Jasmine Magic', 'A-'),
                    (13, 'Mulan Wall', 'O-'),
                    (14, 'Belle Book', 'O-'),
                    (15, 'Raya Dragon', 'AB+'),
                    (16, 'Peter Pan', 'AB-'),
                    (17, 'Merida Greene', 'B+'),
                    (18, 'Bruce Wayne', 'B+'),
                    (19, 'Clark Kent', 'B+'),
                    (20, 'Barry Allen', 'B-'),
                    (21, 'Tony Stark', 'B-'),
                    (22, 'Steve Rogers', 'B-')]
    for (idStore, character, bloodtype) in donor_insert:
        c.execute('''INSERT INTO Donor VALUES (?,?,?);''', (idStore, character, bloodtype))
        
    # Fill in the Patient table
    patient_insert = [(1, 'Arnold Artwood', 'A+'),
                        (2, 'Beatrice Berry', 'B+'),
                        (3, 'Clarence Coldwater', 'AB+'),
                        (4, 'Drake Duckle', 'O+'),
                        (5, 'Elen Eagleton', 'A-'),
                        (6, 'Frank French', 'B-'),
                        (7, 'Gretchen Gamey', 'AB-'),
                        (8, 'Harold Horton', 'O-'),
                        (9, 'Irene Ibola', 'A+'),
                        (10, 'John Jamison', 'B+'),
                        (11, 'Katrina Kelly', 'AB+'),
                        (12, 'Lawrence Lavender', 'O+'),
                        (13, 'Matthew McConaughey', 'A-'),
                        (14, 'Natelie Nevers', 'B-'),
                        (15, 'Orrvile Oggelthorpe', 'AB-'),
                        (16, 'Pamela Parkinson', 'O-'),
                        (17, 'Quinton Quizine', 'A+'),
                        (18, 'Raegan Rizzola', 'B+'),
                        (19, 'Samuel Sanderson', 'AB+'),
                        (20, 'Trinity Thompson', 'O+'),
                        (21, 'Usef Unisone', 'A-'),
                        (22, 'Virginia Vain', 'B-'),
                        (23, 'Wayne Wellington', 'AB-'),
                        (24, 'Xelia Xlan', 'O-'),
                        (25, 'Yale Young', 'A+'),
                        (26, 'Zena Zootopia', 'O+')]
    for (idStore, character, bloodtype) in patient_insert:
        c.execute('''INSERT INTO Patient VALUES (?,?,?);''', (idStore, character, bloodtype))
        
    # Fill in the Donation table
    donation_insert = [(1, '20230701 8:00:00', 1, 'Dr. Bruce Banner', 64, 1),
                            (2, '20230702 9:00:00', 2, 'Dr. Stephan Strange', 63, 1),
                            (3, '20230703 10:00:00', 3, 'Dr. Diana Prince', 62, 1),
                            (4, '20230704 11:00:00', 4, 'Dr. Harleen Quinzel', 61, 1),
                            (5, '20230705 12:00:00', 5, 'Dr. Bruce Banner', 60, 1),
                            (6, '20230706 13:00:00', 6, 'Dr. Stephan Strange', 59, 1),
                            (7, '20230707 14:00:00', 7, 'Dr. Diana Prince', 58, 1),
                            (8, '20230708 15:00:00', 8, 'Dr. Harleen Quinzel', 57, 1),
                            (9, '20230709 16:00:00', 9, 'Dr. Bruce Banner', 56, 1),
                            (10, '20230710 17:00:00', 10, 'Dr. Stephan Strange', 55, 1),
                            (11, '20230711 8:00:00', 11, 'Dr. Diana Prince', 54, 1),
                            (12, '20230712 9:00:00', 12, 'Dr. Harleen Quinzel', 53, 1),
                            (13, '20230713 10:00:00', 13, 'Dr. Bruce Banner', 52, 1),
                            (14, '20230714 11:00:00', 14, 'Dr. Stephan Strange', 51, 1),
                            (15, '20230715 12:00:00', 15, 'Dr. Diana Prince', 50, 1),
                            (16, '20230716 13:00:00', 16, 'Dr. Harleen Quinzel', 49, 1),
                            (17, '20230717 14:00:00', 17, 'Dr. Bruce Banner', 48, 1),
                            (18, '20230718 15:00:00', 18, 'Dr. Stephan Strange', 47, 1),
                            (19, '20230719 16:00:00', 19, 'Dr. Diana Prince', 46, 1),
                            (20, '20230720 17:00:00', 20, 'Dr. Harleen Quinzel', 45, 1),
                            (21, '20230721 8:00:00', 21, 'Dr. Bruce Banner', 44, 1),
                            (22, '20230722 9:00:00', 22, 'Dr. Stephan Strange', 43, 1),
                            (23, '20230723 10:00:00', 8, 'Dr. Diana Prince', 42, 1),
                            (24, '20230724 11:00:00', 9, 'Dr. Harleen Quinzel', 41, 1),
                            (25, '20230725 12:00:00', 10, 'Dr. Bruce Banner', 40, 1),
                            (26, '20230726 13:00:00', 11, 'Dr. Stephan Strange', 39, 1),
                            (27, '20230727 14:00:00', 12, 'Dr. Diana Prince', 38, 1),
                            (28, '20230728 15:00:00', 13, 'Dr. Harleen Quinzel', 37, 1),
                            (29, '20230729 16:00:00', 14, 'Dr. Bruce Banner', 36, 1),
                            (30, '20230730 17:00:00', 8, 'Dr. Stephan Strange', 35, 1),
                            (31, '20230731 8:00:00', 9, 'Dr. Diana Prince', 34, 1),
                            (32, '20230701 9:00:00', 10, 'Dr. Harleen Quinzel', 33, 1),
                            (33, '20230702 10:00:00', 1, 'Dr. Bruce Banner', 32, 1),
                            (34, '20230703 11:00:00', 2, 'Dr. Stephan Strange', 31, 1),
                            (35, '20230704 12:00:00', 3, 'Dr. Diana Prince', 30, 1),
                            (36, '20230705 13:00:00', 1, 'Dr. Harleen Quinzel', 29, 1),
                            (37, '20230706 14:00:00', 2, 'Dr. Bruce Banner', 28, 1),
                            (38, '20230707 15:00:00', 3, 'Dr. Stephan Strange', 27, 1),
                            (39, '20230708 16:00:00', 18, 'Dr. Diana Prince', 26, 1),
                            (40, '20230709 17:00:00', 19, 'Dr. Harleen Quinzel', 25, 1),
                            (41, '20230710 8:00:00', 21, 'Dr. Bruce Banner', 24, 1),
                            (42, '20230711 9:00:00', 22, 'Dr. Stephan Strange', 23, 1)]
    for (idt, tdate, did, character, hid, a) in donation_insert:
        c.execute('''INSERT INTO Donation VALUES (?,?,?,?,?,?);''', (idt, tdate, did, character, hid, a))
        
    # Fill in the Transfusion table
    transfusion_insert = [(1, '20230720 8:00:00', 1, 26, 'Dr. Bruce Banner', 64, 1),
                            (2, '20230721 9:00:00', 2, 25, 'Dr. Stephan Strange', 63, 1),
                            (3, '20230722 10:00:00', 3, 24, 'Dr. Diana Prince', 62, 1),
                            (4, '20230723 11:00:00', 4, 23, 'Dr. Harleen Quinzel', 61, 1)]
    for (idt, tdate, did, pid, character, hid, a) in transfusion_insert:
        c.execute('''INSERT INTO Transfusion VALUES (?,?,?,?,?,?,?);''', (idt, tdate, did, pid, character, hid, a))
        
    # Fill in the Transfer table
    transfer_insert = [(1, '20230701 8:00:00', 25, 40, 14),
                        (2, '20230702 9:00:00', 26, 39, 15),
                        (3, '20230703 10:00:00', 27, 38, 16),
                        (4, '20230704 11:00:00', 28, 37, 17)]
    for (idt, tdate, did, pid, hid) in transfer_insert:
        c.execute('''INSERT INTO Transfer VALUES (?,?,?,?,?);''', (idt, tdate, did, pid, hid))
        
    # Fill in the Complication table
    complication_insert = [(1, 4, 'Throwing up multiple times a day')]
    for (idStore, transfusionid, comp) in complication_insert:
        c.execute('''INSERT INTO Complication VALUES (?,?,?);''', (idStore, transfusionid, comp))
        
    conn.commit()
    conn.close()

# test category table
def test_tables(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    count_cat = 0
    c.execute('''SELECT * FROM Bloodbanks_and_Hospitals WHERE Institution_ID = 64;''')
    if c.fetchone() == (64, 'Hospital', 'Yuma County', 'Wray', 'CO', 76650, 13526, 2500, 441, 7300, 1000, 11000, 1941):
        count_cat = count_cat + 1
        print("First Test Passed!")
    c.execute('''SELECT * FROM Donor WHERE Donor_ID = 22;''')
    if c.fetchone() == (22, 'Steve Rogers', 'B-'):
        count_cat = count_cat + 1
        print("Second Test Passed!")
    c.execute('''SELECT * FROM Patient WHERE Patient_ID = 26;''')
    if c.fetchone() == (26, 'Zena Zootopia', 'O+'):
        count_cat = count_cat + 1
        print("Third Test Passed!")
    c.execute('''SELECT * FROM Donation WHERE Donation_ID = 42;''')
    if c.fetchone() == (42, '20230711 9:00:00', 22, 'Dr. Stephan Strange', 23, 1):
        count_cat = count_cat + 1
        print("Fourth Category Test Passed!")
    c.execute('''SELECT * FROM Transfusion WHERE Transfusion_ID = 4;''')
    if c.fetchone() == (4, '20230723 11:00:00', 4, 23, 'Dr. Harleen Quinzel', 61, 1):
        count_cat = count_cat + 1
        print("Fifth Category Test Passed!")
    c.execute('''SELECT * FROM Transfer WHERE Transfer_ID = 4;''')
    if c.fetchone() == (4, '20230704 11:00:00', 28, 37, 17):
        count_cat = count_cat + 1
        print("Sixth Category Test Passed!")
    c.execute('''SELECT * FROM Complication WHERE Complication_ID = 1;''')
    if c.fetchone() == (1, 4, 'Throwing up multiple times a day'):
        count_cat = count_cat + 1
        print("Seventh Category Test Passed!")
    if count_cat == 7:
        print("All Tests Passed!!!")
    else:
        print("Failed: Test")
    conn.commit()
    conn.close()

# Function to get Donor ID given Donor Name
def getDonorID(db_filename, donorName):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT Donor_ID FROM Donor WHERE Name = ?;''', (donorName,))
    result = c.fetchone()

    # Commit and close connection
    conn.commit()
    conn.close()

    # Return result
    if result:
         return result[0]
    else:
        return None

# Function to get Patient ID given Patient Name
def getPatientID(db_filename, patientName):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT Patient_ID FROM Patient WHERE Name = ?;''', (patientName,))
    result = c.fetchone()

    # Commit and close connection
    conn.commit()
    conn.close()

    # Return result
    if result:
         return result[0]
    else:
        return None

# Function to get Blood Bank ID given Blood Bank Name
def getBloodBankID(db_filename, bloodBankName):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT Institution_ID FROM Bloodbanks_and_Hospitals WHERE Name = ?;''', (bloodBankName,))
    result = c.fetchone()

    # Commit and close connection
    conn.commit()
    conn.close()

    # Return result
    if result:
         return result[0]
    else:
        return None
        
# Function to verify donation entry
def getDonation(db_filename, medicalProfessional):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT * FROM Donation WHERE Medical_Professional = ?;''', (medicalProfessional,))
    result = c.fetchall()

    for line in result:
        print(line)

    # Commit and close connection
    conn.commit()
    conn.close()
    return
        
# Function to verify transfusion entryDono
def getTransfusion(db_filename, medicalProfessional):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT * FROM Transfusion WHERE Medical_Professional = ?;''', (medicalProfessional,))
    result = c.fetchall()

    for line in result:
        print(line)

    # Commit and close connection
    conn.commit()
    conn.close()
    return
        
# Function to enter blood bank in Blood Banks table
def enterBloodBank(db_filename, bloodBankName, bloodBankType, bloodBankCity, bloodBankState):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Get next blood bank ID
    c.execute('''SELECT MAX(Institution_ID) FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchone()
    bloodBankID = result[0] + 1

    # Insert blood bank
    c.execute('''INSERT INTO Bloodbanks_and_Hospitals (Institution_ID, Name, Type, City, State, A_Positive_Units, A_Negative_Units, B_Positive_Units, B_Negative_Units, AB_Positive_Units, AB_Negative_Units, O_Positive_Units, O_Negative_Units) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);''', (bloodBankID, bloodBankName, bloodBankType, bloodBankCity, bloodBankState, 0, 0, 0, 0, 0, 0, 0, 0))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter donor in Donor table
def enterDonor(db_filename, donorName, donorBloodType):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Get next donor ID
    c.execute('''SELECT MAX(Donor_ID) FROM Donor;''')
    result = c.fetchone()
    donorID = result[0] + 1

    # Insert donor
    c.execute('''INSERT INTO Donor (Donor_ID, Name, Blood_Type) VALUES (?,?,?);''', (donorID, donorName, donorBloodType))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter patient in Patient table
def enterPatient(db_filename, patientName, patientBloodType):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Get next patient ID
    c.execute('''SELECT MAX(Patient_ID) FROM Patient;''')
    result = c.fetchone()
    patientID = result[0] + 1

    # Insert patient
    c.execute('''INSERT INTO Patient (Patient_ID, Name, Blood_Type) VALUES (?,?,?);''', (patientID, patientName, patientBloodType))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter donation in Donations table
def enterDonation(db_filename, donorID, bloodBankID, medicalProfessional, quantity, date):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Get next donation ID
    c.execute('''SELECT MAX(Donation_ID) FROM Donation;''')
    result = c.fetchone()
    donationID = result[0] + 1

    # Insert donation
    c.execute('''INSERT INTO Donation (Donation_ID, Donor_ID, Hospital_ID, Medical_Professional, Amount, Date_Time) VALUES (?,?,?,?,?,?);''', (donationID, donorID, bloodBankID, medicalProfessional, quantity, date))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter transfusion in Transfusions table
def enterTransfusion(db_filename, patientID, bloodBankID, donationID, medicalProfessional, quantity, date):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Get next donation ID
    c.execute('''SELECT MAX(Transfusion_ID) FROM Transfusion;''')
    result = c.fetchone()
    transfusionID = result[0] + 1

    # Insert donation
    c.execute('''INSERT INTO Transfusion (Transfusion_ID, Patient_ID, Donation_ID, Hospital_ID, Medical_Professional, Amount, Date_Time) VALUES (?,?,?,?,?,?,?);''', (transfusionID, patientID, donationID, bloodBankID, medicalProfessional, quantity, date))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to get list of Donors
def getDonorsList(db_filename):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Name FROM Donor;''')
    result = c.fetchall()

    # Build donor list
    donorsList = []
    for donor in result:
        donorsList.append(donor[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return donorsList

# Function to get list of Patients
def getPatientsList(db_filename):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Name FROM Patient;''')
    result = c.fetchall()

    # Build donor list
    patientsList = []
    for patient in result:
        patientsList.append(patient[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return patientsList

# Function to get list of Donation IDs
def getDonationIDsList(db_filename):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Donation_ID FROM Donation;''')
    result = c.fetchall()

    # Build donor list
    donationIDsList = []
    for donationID in result:
        donationIDsList.append(donationID[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return donationIDsList

# Function to get list of Blood Banks
def getBloodBanksList(db_filename):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Name FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()

    # Build donor list
    bloodBanksList = []
    for bloodBank in result:
        bloodBanksList.append(bloodBank[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return bloodBanksList

# Function to update Bloodbanks_and_Hospitals Table for a Blood Transfer
def UpdateInstitutionInventory(db_filename, donationid, receivinghospitalID, sendinghospitalID):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Get next transfer ID
    c.execute('''SELECT Donor_ID FROM Donation WHERE Donation_ID = ?;''', (donationid))
    dresult = c.fetchone()
    donorID = dresult[0]
    c.execute('''SELECT Blood_Type FROM Donor WHERE Donor_ID = ?;''', (donorID))
    result = c.fetchone()
    bloodtype = result[0] + 1

    if bloodtype == "A+":
        bt_column = "A_Positive_Units"
    elif bloodtype == "A-":
        bt_column = "A_Negative_Units"
    elif bloodtype == "B+":
        bt_column = "B_Positive_Units"
    elif bloodtype == "B-":
        bt_column = "B_Negative_Units"
    elif bloodtype == "AB+":
        bt_column = "AB_Positive_Units"
    elif bloodtype == "AB-":
        bt_column = "AB_Negative_Units"
    elif bloodtype == "O+":
        bt_column = "O_Positive_Units"
    elif bloodtype == "O-":
        bt_column = "O_Negative_Units"

    # Calculate the new quantity for Receiving Hospital
    c.execute('''SELECT ? FROM Bloodbanks_and_Hospitals WHERE Institution_ID = ?;''', (bt_column, receivinghospitalID))
    result = c.fetchone()
    newamount_r = result[0] + 1
    
    # Calculate the new quantity for Sending Hospital
    c.execute('''SELECT ? FROM Bloodbanks_and_Hospitals WHERE Institution_ID = ?;''', (bt_column, sendinghospitalID))
    result = c.fetchone()
    newamount_s = result[0] - 1

    # Update Receiving Hospital
    c.execute('''UPDATE Bloodbanks_and_Hospitals SET ? = ? WHERE Institution_ID = ?;''', (bt_column, newamount_r, receivinghospitalID))
    
    # Update Sending Hospital
    c.execute('''UPDATE Bloodbanks_and_Hospitals SET ? = ? WHERE Institution_ID = ?;''', (bt_column, newamount_s, sendinghospitalID))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter blood transfer in Transfer table
def enterTransfer(db_filename, donationID, receivinghospitalID, sendinghospitalID):

    # Initialize connection
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Get next transfer ID
    c.execute('''SELECT MAX(Transfer_ID) FROM Transfer;''')
    result = c.fetchone()
    transferID = result[0] + 1
    
    # Get current datetime
    dt_now = datetime.datetime.now()

    # Insert transfer
    c.execute('''INSERT INTO Transfer (Transfer_ID, Date_Time, Donation_ID, Receiving_Hospital_ID, Sending_Hospital_ID) VALUES (?,?,?,?,?);''', (transferID, dt_now, donationID, receivinghospitalID, sendinghospitalID))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to get A postive units
def getBloodAList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all A positive units
    c.execute('''SELECT A_POSITIVE_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A positive units:
def getTotalAPositiveUnits(db_filename):
    a_positive_units = getBloodAList(db_filename)
    total_a_positive_units = sum(a_positive_units)
    return total_a_positive_units

# Function to get B positive units
def getBloodBList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all B positive units
    c.execute('''SELECT B_Positive_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total b positive units:
def getTotalBPositiveUnits(db_filename):
    b_positive_units = getBloodBList(db_filename)
    total_b_positive_units = sum(b_positive_units)
    return total_b_positive_units

# Function to get AB positive units
def getBloodABList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all AB psoitive units
    c.execute('''SELECT AB_Positive_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total AB positive units:
def getTotalABPositiveUnits(db_filename):
    ab_positive_units = getBloodABList(db_filename)
    total_ab_positive_units = sum(ab_positive_units)
    return total_ab_positive_units

# Function to get O positive units
def getBloodOList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all O positive units
    c.execute('''SELECT O_Positive_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total O positive units:
def getTotalOPositiveUnits(db_filename):
    o_positive_units = getBloodOList(db_filename)
    total_o_positive_units = sum(o_positive_units)
    return total_o_positive_units

# Function to get A negative units
def getBloodANList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all A negative units
    c.execute('''SELECT A_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A Negative units:
def getTotalANegativeUnits(db_filename):
    a_negative_units = getBloodANList(db_filename)
    total_a_negative_units = sum(a_negative_units)
    return total_a_negative_units

# Function to get B negative units
def getBloodBNList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all donor names
    c.execute('''SELECT B_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total B Negative units:
def getTotalBNegativeUnits(db_filename):
    b_negative_units = getBloodBNList(db_filename)
    total_b_negative_units = sum(b_negative_units)
    return total_b_negative_units

# Function to get AB negative units
def getBloodABNList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT AB_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A Negative units:
def getTotalABNegativeUnits(db_filename):
    ab_negative_units = getBloodANList(db_filename)
    total_ab_negative_units = sum(ab_negative_units)
    return total_ab_negative_units

# Function to get O negative units
def getBloodONList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT O_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A Negative units:
def getTotalONegativeUnits(db_filename):
    o_negative_units = getBloodONList(db_filename)
    total_o_negative_units = sum(o_negative_units)
    return total_o_negative_units

# Function to get all bank ids
def getBloodID(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT Institution_ID FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# Function to get city and state 
def getAddress(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT City, State FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# Function to return blood bank types
def getBankType(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT Type FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# Function to get all data from the Donation table for a given blood bank ID
def getDonationTable(db_filename, bankID):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Donation WHERE Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all data from the Transfusion table for a given blood bank ID
def getTransfusionTable(db_filename, bankID):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Transfusion WHERE Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all incoming transfer data from the Transfer table for a given blood bank ID
def getIncomingTransferTable(db_filename, bankID):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Transfer WHERE Receiving_Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all outgoing transfer data from the Transfer table for a given blood bank ID
def getOutgoingTransferTable(db_filename, bankID):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Transfer WHERE Sending_Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get list of Blood Banks and their IDs
def getBloodBanksIDsList(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT Name, Institution_ID FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all donor data
def getDonors(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Donor;''')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


# Function to get all patient data
def getPatients(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Patient;''')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


#Function to enter Comments on complication_report.html
def enterComments(db_filename, transfusion_id, comments):
    try:
        # Connect to the database
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()

        # Check if the Transfusion_ID exists in the Transfusion table
        c.execute("SELECT * FROM Transfusion WHERE Transfusion_ID=?", (transfusion_id,))
        result = c.fetchone()

        if result is None:
            print(f"Transfusion with ID {transfusion_id} not found.")
            return False
        else:
            # If the Transfusion_ID exists, insert the data into the Complication table
            c.execute("INSERT INTO Complication (Transfusion_ID, Comments) VALUES (?, ?)",
                      (transfusion_id, comments))
            conn.commit()
            print("Comments added successfully.")
            return True

        # Close the database connection
        conn.close()

    except sqlite3.Error as e:
        print("Error:", e)
        return False

#Function to get Comments for view_report.html
def getComments(db_filename, transfusion_id):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Retrieve the Complication_ID and Comments for the given transfusion_id from the Complication table
    c.execute('''SELECT Complication_ID, Comments FROM Complication WHERE Transfusion_ID = ?;''', (transfusion_id,))
    result = c.fetchone()
    
    conn.close()
    
    if result:
        complication_id, comments = result
        return complication_id, comments
    else:
        return None, None
    
# Code to run to set up database
if __name__ == "__main__":
    space_monkeys_db = 'space_monkeys_db'
    create(space_monkeys_db)
    fill(space_monkeys_db)
    test_tables(space_monkeys_db)
    
