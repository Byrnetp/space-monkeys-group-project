## CS 3308 Group Project
## Team 2: Space Monkeys
## sm_dbAPI test code
## Last Update: Travis Byrne, 3 August 2023
## USAGE: python3 -m pytest

# Import support routines from sm_dbAPI.py
import sm_dbAPI
import sqlite3
import unittest
import os

class Test_sm_dbAPI(unittest.TestCase):
    
    # Create database and fill with test data
    def setUp(self):
        sm_dbAPI.create("sm_test.db")
        sm_dbAPI.fill("sm_test.db")

    def tearDown(self):
        
        # Remove test database
        try:
            os.remove("sm_test.db")
        except:
            print("An exception occurred during teardown")

    # Test getDonorID function in dbAPI
    def test_getDonorID(self):

        # List of Donors, Donor IDs, and Blood Types used in db creation
        test_parameters = [
            (1, 'Bugs Bunny', 'A+'),
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
            (22, 'Steve Rogers', 'B-'),
            ]

        # Test that correct ID is returned by getDonorID function
        for parameter in test_parameters:
            result = sm_dbAPI.getDonorID("sm_test.db", parameter[1])
            self.assertEqual(parameter[0], result)
        
        # Test that None is returned by getDonorID when bogus name is given
        result = sm_dbAPI.getDonorID("sm_test.db", "not a donor name")
        self.assertEqual(None, result)

    # Test getPatientID function in dbAPI
    def test_getPatientID(self):

        # List of Patients, Patient IDs, and Blood Types used in db creation
        test_parameters = [
            (1, 'Arnold Artwood', 'A+'),
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
            (26, 'Zena Zootopia', 'O+'),
        ]

        # Test that correct ID is returned by getPatientID function
        for parameter in test_parameters:
            result = sm_dbAPI.getPatientID("sm_test.db", parameter[1])
            self.assertEqual(parameter[0], result)
        
        # Test that None is returned by getPatientID when bogus name is given
        result = sm_dbAPI.getPatientID("sm_test.db", "not a patient name")
        self.assertEqual(None, result)

    # Test getBloodBankID function in dbAPI
    def test_getBloodBankID(self):

        # List of Blood Banks and Blood Banks IDs used in db creation
        test_parameters = [
            (1, 'Hospital', 'Adams County', 'Brighton', 'CO', 10500, 1853, 18250, 3221, 1000, 7300, 80300, 14171),
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
            (64, 'Hospital', 'Yuma County', 'Wray', 'CO', 76650, 13526, 2500, 441, 7300, 1000, 11000, 1941),
        ]

        # Test that correct ID is returned by getBloodBankID function
        for parameter in test_parameters:
            result = sm_dbAPI.getBloodBankID("sm_test.db", parameter[2])
            self.assertEqual(parameter[0], result)
        
        # Test that None is returned by getBloodBankID when bogus name is given
        result = sm_dbAPI.getBloodBankID("sm_test.db", "not a blood bank name")
        self.assertEqual(None, result)

    # Test enterBloodBank function in dbAPI
    def test_enterBloodBank(self):

        # List of data to enter
        test_parameters = [
            ("sm_test.db", "Hollywood Blood Bank", "Private", "Los Angeles", "CA"),
            ("sm_test.db", "Bollywood Blood Bank", "International", "Mumbai", "IN"),
        ]

        # Enter data
        for parameter in test_parameters:
            sm_dbAPI.enterBloodBank(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4])
        
        # Test that data is correctly entered
        conn = sqlite3.connect("sm_test.db")
        c = conn.cursor()
        for parameter in test_parameters:
            c.execute('''SELECT * FROM Bloodbanks_and_Hospitals WHERE Name = ?;''', (parameter[1],))
            (_, res_type, res_name, res_city, res_state, _, _, _, _, _, _, _, _) = c.fetchone()
            self.assertEqual(parameter[1], res_name)
            self.assertEqual(parameter[2], res_type)
            self.assertEqual(parameter[3], res_city)
            self.assertEqual(parameter[4], res_state)
        conn.close()

    # Test enterDonor function in dbAPI
    def test_enterDonor(self):

        # List of data to enter
        test_parameters = [
            ("sm_test.db", "SpaceMonkey1", "A+"),
            ("sm_test.db", "SpaceMonkey2", "B-"),
        ]

        # Enter data
        for parameter in test_parameters:
            sm_dbAPI.enterDonor(parameter[0], parameter[1], parameter[2])
        
        # Test that data is correctly entered
        conn = sqlite3.connect("sm_test.db")
        c = conn.cursor()
        for parameter in test_parameters:
            c.execute('''SELECT * FROM Donor WHERE Name = ?;''', (parameter[1],))
            (_, res_name, res_type) = c.fetchone()
            self.assertEqual(parameter[1], res_name)
            self.assertEqual(parameter[2], res_type)
        conn.close()

    # Test enterPatient function in dbAPI
    def test_enterPatient(self):

        # List of data to enter
        test_parameters = [
            ("sm_test.db", "SpaceMonkey1", "A+"),
            ("sm_test.db", "SpaceMonkey2", "B-"),
        ]

        # Enter data
        for parameter in test_parameters:
            sm_dbAPI.enterPatient(parameter[0], parameter[1], parameter[2])
        
        # Test that data is correctly entered
        conn = sqlite3.connect("sm_test.db")
        c = conn.cursor()
        for parameter in test_parameters:
            c.execute('''SELECT * FROM Patient WHERE Name = ?;''', (parameter[1],))
            (_, res_name, res_type) = c.fetchone()
            self.assertEqual(parameter[1], res_name)
            self.assertEqual(parameter[2], res_type)
        conn.close()

    # Test enterDonation function in dbAPI
    def test_enterDonation(self):

        # List of data to enter
        test_parameters = [
            ("sm_test.db", 4, 1, "SpaceMonkey1", 1, "2023-07-01 8:00:00"),
            ("sm_test.db", 3, 2, "SpaceMonkey2", 1, "2023-07-02 9:00:00"),
        ]

        # Enter data
        for parameter in test_parameters:
            sm_dbAPI.enterDonation(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4], parameter[5])
        
        # Test that data is correctly entered
        conn = sqlite3.connect("sm_test.db")
        c = conn.cursor()
        for parameter in test_parameters:
            c.execute('''SELECT * FROM Donation WHERE Medical_Professional = ?;''', (parameter[3],))
            (_, res_date, res_donorID, res_medicalProfessional, res_bloodBankID, res_quantity) = c.fetchone()
            self.assertEqual(parameter[1], res_donorID)
            self.assertEqual(parameter[2], res_bloodBankID)
            self.assertEqual(parameter[3], res_medicalProfessional)
            self.assertEqual(parameter[4], res_quantity)
            self.assertEqual(parameter[5], res_date)
        conn.close()

    # Test enterTransfusion function in dbAPI
    def test_enterTransfusion(self):

        # List of data to enter
        test_parameters = [
            ("sm_test.db", 4, 1, 5, "SpaceMonkey1", 1, "2023-07-01 8:00:00"),
            ("sm_test.db", 3, 2, 6, "SpaceMonkey2", 1, "2023-07-02 9:00:00"),
        ]

        # Enter data
        for parameter in test_parameters:
            sm_dbAPI.enterTransfusion(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4], parameter[5], parameter[6])
        
        # Test that data is correctly entered
        conn = sqlite3.connect("sm_test.db")
        c = conn.cursor()
        for parameter in test_parameters:
            c.execute('''SELECT * FROM Transfusion WHERE Medical_Professional = ?;''', (parameter[4],))
            (_, res_date, res_donationID, res_patientID, res_medicalProfessional, res_bloodBankID, res_quantity) = c.fetchone()
            self.assertEqual(parameter[1], res_patientID)
            self.assertEqual(parameter[2], res_bloodBankID)
            self.assertEqual(parameter[3], res_donationID)
            self.assertEqual(parameter[4], res_medicalProfessional)
            self.assertEqual(parameter[5], res_quantity)
            self.assertEqual(parameter[6], res_date)
        conn.close()

    # Test getDonorsList function in dbAPI
    def test_getDonorsList(self):

        # List of expected data
        test_parameters = ['Bugs Bunny', 'Daffy Duck', 'Porky Pig', 'Elmer Fudd', 'Tweety Bird', 'Yosemite Sam', 'Lola Bunny', 'Snow White', 'Tinker Bell', 'Cinderlla Castle', 'Ariel Mermaid', 'Jasmine Magic', 'Mulan Wall', 'Belle Book', 'Raya Dragon', 'Peter Pan', 'Merida Greene', 'Bruce Wayne', 'Clark Kent', 'Barry Allen', 'Tony Stark', 'Steve Rogers']

        # Get data
        res = sm_dbAPI.getDonorsList("sm_test.db")

        # Test data is correct
        for name in res:
            self.assertIn(name, test_parameters)

    # Test getPatientsList function in dbAPI
    def test_getPatientsList(self):

        # List of expected data
        test_parameters = ['Arnold Artwood', 'Beatrice Berry', 'Clarence Coldwater', 'Drake Duckle', 'Elen Eagleton', 'Frank French', 'Gretchen Gamey', 'Harold Horton', 'Irene Ibola', 'John Jamison', 'Katrina Kelly', 'Lawrence Lavender', 'Matthew McConaughey', 'Natelie Nevers', 'Orrvile Oggelthorpe', 'Pamela Parkinson', 'Quinton Quizine', 'Raegan Rizzola', 'Samuel Sanderson', 'Trinity Thompson', 'Usef Unisone', 'Virginia Vain', 'Wayne Wellington', 'Xelia Xlan', 'Yale Young', 'Zena Zootopia']

        # Get data
        res = sm_dbAPI.getPatientsList("sm_test.db")

        # Test data is correct
        for name in res:
            self.assertIn(name, test_parameters)

    # Test getDonationIDsList function in dbAPI
    def test_getDonationIDsList(self):

        # List of expected data
        test_parameters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]

        # Get data
        res = sm_dbAPI.getDonationIDsList("sm_test.db")

        # Test data is correct
        for donationID in res:
            self.assertIn(donationID, test_parameters)

    # Test getBloodBanksList function in dbAPI
    def test_getBloodBanksList(self):

        # List of expected data
        test_parameters = ['Adams County', 'Alamosa County', 'Arapahoe County', 'Archuleta County', 'Baca County', 'Bent County', 'Boulder County', 'Broomfield County', 'Chaffee County', 'Cheyenne County', 'Clear Creek County', 'Conejos County', 'Costilla County', 'Crowley County', 'Custer County', 'Delta County', 'Denver County', 'Dolores County', 'Douglas County', 'Eagle County', 'El Paso County', 'Elbert County', 'Fremont County', 'Garfield County', 'Gilpin County', 'Grand County', 'Gunnison County', 'Hinsdale County', 'Huerfano County', 'Jackson County', 'Jefferson County', 'Kiowa County', 'Kit Carson County', 'La Plata County', 'Lake County', 'Larimer County', 'Las Animas County', 'Lincoln County', 'Logan County', 'Mesa County', 'Mineral County', 'Moffat County', 'Montezuma County', 'Montrose County', 'Morgan County', 'Otero County', 'Ouray County', 'Park County', 'Phillips County', 'Pitkin County', 'Prowers County', 'Pueblo County', 'Rio Blanco County', 'Rio Grande County', 'Routt County', 'Saguache County', 'San Juan County', 'San Miguel County', 'Sedgwick County', 'Summit County', 'Teller County', 'Washington County', 'Weld County', 'Yuma County']

        # Get data
        res = sm_dbAPI.getBloodBanksList("sm_test.db")

        # Test data is correct
        for name in res:
            self.assertIn(name, test_parameters)

    # Test getDonationTable function in dbAPI
    def test_getDonationTable(self):

        # List of expected data
        test_parameters = [(1, '2023-07-01 8:00:00', 1, 'Dr. Bruce Banner', 64, 1),
                            (2, '2023-07-02 9:00:00', 2, 'Dr. Stephan Strange', 63, 1),
                            (3, '2023-07-03 10:00:00', 3, 'Dr. Diana Prince', 62, 1),
                            (4, '2023-07-04 11:00:00', 4, 'Dr. Harleen Quinzel', 61, 1),
                            (5, '2023-07-05 12:00:00', 5, 'Dr. Bruce Banner', 60, 1),
                            (6, '2023-07-06 13:00:00', 6, 'Dr. Stephan Strange', 59, 1),
                            (7, '2023-07-07 14:00:00', 7, 'Dr. Diana Prince', 58, 1),
                            (8, '2023-07-08 15:00:00', 8, 'Dr. Harleen Quinzel', 57, 1),
                            (9, '2023-07-09 16:00:00', 9, 'Dr. Bruce Banner', 56, 1),
                            (10, '2023-07-10 17:00:00', 10, 'Dr. Stephan Strange', 55, 1),
                            (11, '2023-07-11 8:00:00', 11, 'Dr. Diana Prince', 54, 1),
                            (12, '2023-07-12 9:00:00', 12, 'Dr. Harleen Quinzel', 53, 1),
                            (13, '2023-07-13 10:00:00', 13, 'Dr. Bruce Banner', 52, 1),
                            (14, '2023-07-14 11:00:00', 14, 'Dr. Stephan Strange', 51, 1),
                            (15, '2023-07-15 12:00:00', 15, 'Dr. Diana Prince', 50, 1),
                            (16, '2023-07-16 13:00:00', 16, 'Dr. Harleen Quinzel', 49, 1),
                            (17, '2023-07-17 14:00:00', 17, 'Dr. Bruce Banner', 48, 1),
                            (18, '2023-07-18 15:00:00', 18, 'Dr. Stephan Strange', 47, 1),
                            (19, '2023-07-19 16:00:00', 19, 'Dr. Diana Prince', 46, 1),
                            (20, '2023-07-20 17:00:00', 20, 'Dr. Harleen Quinzel', 45, 1),
                            (21, '2023-07-21 8:00:00', 21, 'Dr. Bruce Banner', 44, 1),
                            (22, '2023-07-22 9:00:00', 22, 'Dr. Stephan Strange', 43, 1),
                            (23, '2023-07-23 10:00:00', 8, 'Dr. Diana Prince', 42, 1),
                            (24, '2023-07-24 11:00:00', 9, 'Dr. Harleen Quinzel', 41, 1),
                            (25, '2023-07-25 12:00:00', 10, 'Dr. Bruce Banner', 40, 1),
                            (26, '2023-07-26 13:00:00', 11, 'Dr. Stephan Strange', 39, 1),
                            (27, '2023-07-27 14:00:00', 12, 'Dr. Diana Prince', 38, 1),
                            (28, '2023-07-28 15:00:00', 13, 'Dr. Harleen Quinzel', 37, 1),
                            (29, '2023-07-29 16:00:00', 14, 'Dr. Bruce Banner', 36, 1),
                            (30, '2023-07-30 17:00:00', 8, 'Dr. Stephan Strange', 35, 1),
                            (31, '2023-07-31 8:00:00', 9, 'Dr. Diana Prince', 34, 1),
                            (32, '2023-07-01 9:00:00', 10, 'Dr. Harleen Quinzel', 33, 1),
                            (33, '2023-07-02 10:00:00', 1, 'Dr. Bruce Banner', 32, 1),
                            (34, '2023-07-03 11:00:00', 2, 'Dr. Stephan Strange', 31, 1),
                            (35, '2023-07-04 12:00:00', 3, 'Dr. Diana Prince', 30, 1),
                            (36, '2023-07-05 13:00:00', 1, 'Dr. Harleen Quinzel', 29, 1),
                            (37, '2023-07-06 14:00:00', 2, 'Dr. Bruce Banner', 28, 1),
                            (38, '2023-07-07 15:00:00', 3, 'Dr. Stephan Strange', 27, 1),
                            (39, '2023-07-08 16:00:00', 18, 'Dr. Diana Prince', 26, 1),
                            (40, '2023-07-09 17:00:00', 19, 'Dr. Harleen Quinzel', 25, 1),
                            (41, '2023-07-10 8:00:00', 21, 'Dr. Bruce Banner', 24, 1),
                            (42, '2023-07-11 9:00:00', 22, 'Dr. Stephan Strange', 23, 1)]

        # Test data is correct
        for i in range(1, len(test_parameters)):

            # Get data for entry i in test_parameters
            data = sm_dbAPI.getDonationTable("sm_test.db", test_parameters[i][4])

            self.assertIn(test_parameters[i], data)
    
    # Test getTransfusionTable function in dbAPI
    def test_getTransfusionTable(self):

        # List of expected data
        test_parameters = [(1, '2023-07-20 8:00:00', 1, 26, 'Dr. Bruce Banner', 64, 1),
                            (2, '2023-07-21 9:00:00', 2, 25, 'Dr. Stephan Strange', 63, 1),
                            (3, '2023-07-22 10:00:00', 3, 24, 'Dr. Diana Prince', 62, 1),
                            (4, '2023-07-23 11:00:00', 4, 23, 'Dr. Harleen Quinzel', 61, 1)]

        # Test data is correct
        for i in range(1, len(test_parameters)):

            # Get data for entry i in test_parameters
            data = sm_dbAPI.getTransfusionTable("sm_test.db", test_parameters[i][5])

            self.assertIn(test_parameters[i], data)
    
    # Test getIncomingTransferTable function in dbAPI
    def test_getIncomingTransferTable(self):

        # List of expected data
        test_parameters = [(1, '2023-07-01 8:00:00', 25, 40, 14),
                        (2, '2023-07-02 9:00:00', 26, 39, 15),
                        (3, '2023-07-03 10:00:00', 27, 38, 16),
                        (4, '2023-07-04 11:00:00', 28, 37, 17)]

        # Test data is correct
        for i in range(1, len(test_parameters)):

            # Get data for entry i in test_parameters
            data = sm_dbAPI.getIncomingTransferTable("sm_test.db", test_parameters[i][3])

            self.assertIn(test_parameters[i], data)
    
    # Test getOutgoingTransferTable function in dbAPI
    def test_getOutgoingTransferTable(self):

        # List of expected data
        test_parameters = [(1, '2023-07-01 8:00:00', 25, 40, 14),
                        (2, '2023-07-02 9:00:00', 26, 39, 15),
                        (3, '2023-07-03 10:00:00', 27, 38, 16),
                        (4, '2023-07-04 11:00:00', 28, 37, 17)]

        # Test data is correct
        for i in range(1, len(test_parameters)):

            # Get data for entry i in test_parameters
            data = sm_dbAPI.getOutgoingTransferTable("sm_test.db", test_parameters[i][4])

            self.assertIn(test_parameters[i], data)
    
    # Test getBloodBanksIDsList function in dbAPI
    def test_getBloodBanksIDsList(self):

        # List of expected data
        test_parameters = [('Adams County', 1), ('Alamosa County', 2), ('Arapahoe County', 3), ('Archuleta County', 4), ('Baca County', 5), ('Bent County', 6), ('Boulder County', 7), ('Broomfield County', 8), ('Chaffee County', 9), ('Cheyenne County', 10), ('Clear Creek County', 11), ('Conejos County', 12), ('Costilla County', 13), ('Crowley County', 14), ('Custer County', 15), ('Delta County', 16), ('Denver County', 17), ('Dolores County', 18), ('Douglas County', 19), ('Eagle County', 20), ('El Paso County', 21), ('Elbert County', 22), ('Fremont County', 23), ('Garfield County', 24), ('Gilpin County', 25), ('Grand County', 26), ('Gunnison County', 27), ('Hinsdale County', 28), ('Huerfano County', 29), ('Jackson County', 30), ('Jefferson County', 31), ('Kiowa County', 32), ('Kit Carson County', 33), ('La Plata County', 34), ('Lake County', 35), ('Larimer County', 36), ('Las Animas County', 37), ('Lincoln County', 38), ('Logan County', 39), ('Mesa County', 40), ('Mineral County', 41), ('Moffat County', 42), ('Montezuma County', 43), ('Montrose County', 44), ('Morgan County', 45), ('Otero County', 46), ('Ouray County', 47), ('Park County', 48), ('Phillips County', 49), ('Pitkin County', 50), ('Prowers County', 51), ('Pueblo County', 52), ('Rio Blanco County', 53), ('Rio Grande County', 54), ('Routt County', 55), ('Saguache County', 56), ('San Juan County', 57), ('San Miguel County', 58), ('Sedgwick County', 59), ('Summit County', 60), ('Teller County', 61), ('Washington County', 62), ('Weld County', 63), ('Yuma County', 64)]

        # Get data
        res = sm_dbAPI.getBloodBanksIDsList("sm_test.db")

        # Test data is correct
        for name in res:
            self.assertIn(name, test_parameters)
    
    # Test getDonors function in dbAPI
    def test_getDonors(self):

        # List of expected data
        test_parameters = [(1, 'Bugs Bunny', 'A+'),
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

        # Get data
        data = sm_dbAPI.getDonors("sm_test.db")

        # Test that the data is correct
        self.assertEqual(data, test_parameters)
    
    # Test getDonors function in dbAPI
    def test_getPatients(self):

        # List of expected data
        test_parameters = [(1, 'Arnold Artwood', 'A+'),
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

        # Get data
        data = sm_dbAPI.getPatients("sm_test.db")

        # Test that the data is correct
        self.assertEqual(data, test_parameters)

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
