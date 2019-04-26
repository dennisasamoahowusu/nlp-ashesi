-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2019 at 07:43 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 5.6.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ashesi_bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `about_ashesi`
--

CREATE TABLE `about_ashesi` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `about_ashesi`
--

INSERT INTO `about_ashesi` (`id`, `entity`, `responses`) VALUES
(1, 'mission', 'Ashesi Mission:\r\nTo educate a new generation of ethical, entrepreneurial leaders in Africa'),
(2, 'vision', 'Our vision is an African renaissance driven by a new generation of ethical, entrepreneurial leaders. We aim to educate such leaders, and to drive a movement in African higher education to scale up the education of such leaders'),
(3, 'population', ' Ashesi  has 1005 students, and over 1,200 alumni'),
(4, 'enrollment', '1005 students\r\n47% are women\r\n45% of students are on scholarships\r\n17% are international students\r\nOver 20 countries are represented.\r\nCountries most represented: Ghana, Gambia, Kenya, Nigeria, Rwanda, Uganda and Zimbabwe'),
(5, 'quick_facts', 'Ashesi Quick Facts:\r\n100 acres\r\n13% solar-powered\r\nRain water storage: 1.057 million liters\r\n465 MBps internet bandwidth \r\nWi-Fi: in academic buildings and residence halls\r\nOn-campus:\r\nHousing for 50% of students\r\nSports Centre \r\nhealth centre\r\nwaste treatment centre\r\n'),
(6, 'founder', 'Dr. Patrick Awuah, is the founder of Ashesi University.'),
(7, 'history', '2002: Ashesi University commenced, with a pioneering class of 30 students in a rented house.\r\n2008: Students vote to adopt Examination Honour Code \r\n2009:  Permanent campus construction in Berekuso started.\r\n2011: Moved in to new campus\r\n2018:  Won a Presidential Charter'),
(9, 'core_values', 'scholarship, leadership and citizenship'),
(10, 'population_alumni', 'over 1200 Ashesi graduates');

-- --------------------------------------------------------

--
-- Table structure for table `admission`
--

CREATE TABLE `admission` (
  `ID` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admission`
--

INSERT INTO `admission` (`ID`, `entity`, `responses`) VALUES
(1, 'academic_qualification', '1. Completed application form and personal essays.\r\n2. High School transcripts or report cards for at least six terms.\r\n3. One of the following examination results is required:\r\ni. WASSCE\r\nii. Six IGCSE (G.C.E. O-Level) & A\'Level\r\niii. International Baccalaureate (IB) Diploma\r\niv. American / Canadian High School Diploma\r\nv. French Baccalaureate(in English(certified))\r\nvi. Other equivalent exam results approved by the National Accreditation Board of Ghana.\r\n\r\nFor more infor:\r\n\r\nwww.ashesi.edu.gh/admissions/selection-criteria.html\r\n\r\n'),
(2, 'selection_criteria', 'To be admitted, we consider:\r\n1. academic merit\r\n2. character\r\n3. extracurricular activities engagement\r\n4. Volunteer experience\r\n5. committed to strengthening Ashesi experience\r\n\r\n\r\n\r\n\r\n\r\n'),
(4, 'transfer_students', 'We accept transfer students from other universities to Ashesi.\r\nadmissions office and academic departments process their applications.\r\nRequirements:\r\n\r\n1.provide official transcripts from each college or university attended.\r\n\r\n2.eligible to have one year of study waived at Ashesi\r\n\r\n '),
(5, 'contact_admin', '1 University Avenue, Berekuso\r\nPMB CT 3, Cantonments\r\nAccra, Ghana\r\n\r\nFront Office:  \r\nT: +233 (302) 610 330\r\nT: +233­ ?302 974 980\r\nE: info@ashesi.edu.gh\r\n\r\n\r\nAdmissions Office\r\nTel: +233 20 437 4374\r\nTel: +233 50 131 8961\r\nTel: +233 50 131 9264 \r\nE: admissions@ashesi.edu.gh \r\n\r\n'),
(6, 'admission_open', 'Ashesi Admission is already open for 2019 admissions.\r\nEarly Deadline: 28th March 2019\r\n\r\n• Regular Deadline: 27th June 2019\r\n\r\n• Late Deadline: 22nd August 2019\r\nThe Late Admissions period attracts an extra GHc 50. \r\nNB Late Admission Period:No scholarship & International application.\r\n'),
(7, 'deadline', '2019 APPLICATION DEADLINES \r\n• Early Admissions Application Deadline: 28th March 2019.\r\n• Regular Admissions Application Deadline: 27th June 2019.\r\n• Late Admissions Application Deadline: 22nd August 2019\r\nWe do not accept scholarship or international applications for late submissions.'),
(8, 'text_books', 'Tuition fee covers textbooks needed.\r\nAll textbooks are provided by the school.\r\n'),
(9, 'academic_qualifications_engineering', 'WASSCE: 3 core subjects including Mathematics, English and Science, and three elective subjects including Elective Mathematics and Physics, with a C6 or better in each of them.\r\n\r\nA-Level: Three A-Level passes\r\n (A-D) including Mathematics and   Physics,\r\n six IGCSE (G.C.E. O-Level) passes including English, and Science \r\n A grade of D or better in Further Mathematics/Mathematics\r\n\r\nInternational Baccalaureate (IB) Diploma: \r\nMathematics SL with a 5 or better, or Mathematics HL with a 3 or b;\r\nPhysics SL with a 5 or better,  \r\nPhysics HL with a 3 or better is acceptable to fulfil the entry physics requirement. '),
(10, 'academic_qualification_nonGhanaian', 'The standard admissions requirements and :\r\n\r\nCertified Translation:\r\nAll documents and transcripts in English and certified as copies of the original document(s).\r\n\r\nEvidence of English Language: proficiency: International students for who English was not a language of instruction during high school, \r\nProvide:\r\nForeign Language (TOEFL), International English Language Testing System (IELTS)\r\n\r\n '),
(11, 'personality', 'prospective students must place an emphasis on sharing information with us that highlights their character and personality. Did you actively play any sport in high school? \r\nWere you a member of the debate club? \r\nDid you do some work when you were not in school?'),
(12, 'commencement', 'Ashesi University started in a rented home in 2002, with 30 pioneer students.'),
(13, 'population', 'ashesi has over 1000 students, and over 1,200 alumni'),
(14, 'most_represented_countries', 'Ghana, Gambia, Kenya, Nigeria, Rwanda, Uganda and Zimbabwe'),
(15, 'leadership_teams', '37 full-time faculty\r\n14 adjunct faculty\r\n34 faculty interns (teaching assistants)\r\n78 administrative staff\r\n41% women on university team\r\n60% women on University Executive Team\r\n55% women on the Board of Directors'),
(16, 'Ashesi_land', ' 100 acres in Berekuso overlooking Ghana\'s capital city of Accra');

-- --------------------------------------------------------

--
-- Table structure for table `application`
--

CREATE TABLE `application` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `application`
--

INSERT INTO `application` (`id`, `entity`, `responses`) VALUES
(1, 'application_process', 'How to Apply in 3 Steps\r\n\r\n(1) Start Online Application or Paper Application\r\n(2)Pay Application Fees\r\n(3) Submit completed applications\r\n\r\n(1) Start Online Application or Paper Application\r\n\r\nOnline Application:\r\nClick here to open Online Application Form\r\nPaper Application: \r\nIf you prefer to fill a paper application, download and complete the forms below: \r\nDownload Application Form\r\nDownload Scholarship Form\r\n\r\nPlease note that paper applications may delay processing for up to a month and may result in repetitive request for information.\r\n  \r\n\r\n(2) Pay Application Fees\r\nGHs100 for Ghanaian nationals; $50 for international applicants. \r\n(How to pay application fees)\r\nThe Late Admissions period attracts an extra GHs50. We also do not accept scholarship and international applications for the Late Admissions period.\r\nApplication Payments can be made as follows\r\nMTNMobile Money\r\nTransfer application fee to merchant mobile number: 024 526 4831?\r\nName of recipient should be Ashesi University College?\r\nApplicants should quote the following information on their application form or in the task box in the online application portal:\r\nMobile number used for transaction by applicant\r\nTransaction ID\r\nReference Number (Applicant’s Name should be used as the reference)\r\nexpressPay\r\nFor Applicants who will like to pay via Visa, Mastercard, Amex, Discover or Mobile Money (MTN, Airtel Money, Tigo Cash, Vodaphone Cash) see link below. https://expresspaygh.com/ashesi. Applicants should quote the expressPay generated transaction reference number on their application form (paper applications) or in the task box on the online application portal.\r\nDirect Deposit/Rapid Transfer at any Ecobank Branch in Ghana and West Africa\r\nAccount Name: Ashesi Admission fees\r\nAccount Number: 02000 144 116 009 05\r\nBank: Ecobank\r\nBranch: Osu\r\nCurrency: Ghana Cedi\r\nWire Transfer from within West Africa\r\n   SWIFT code: ECOCGHAC\r\nAccount Name: Ashesi University College\r\nAccount Number: 02010 144 116 009 01\r\nBank: ECOBANK, PMB CT443, ACCRA-GHANA\r\nBranch: Osu\r\nCurrency: US Dollar \r\nInternational Payments (All other countries)\r\n  SWIFT code: ECOCGHAC\r\nAccount Name: Ashesi University College\r\nAccount Number: 02010 144 116 009 01\r\nBank: ECOBANK, PMB CT443, ACCRA-GHANA\r\nBranch: Osu\r\n \r\n* Attach a copy of your payment receipt to your complete application. Failure to follow instructions stated above will result in the delay of processing your application\r\n(3) Submit completed applications\r\n\r\nBy Post:\r\nAdmissions Office \r\nAshesi University College\r\nPMB CT3, Cantonments,\r\nAccra, Ghana\r\n\r\nBy E-mail\r\nScan completed application and email to: \r\nadmissions@ashesi.edu.gh\r\n\r\nIn-Person\r\nAshesi University College, \r\n1 University Avenue, \r\nBerekuso, Ghana\r\nClick here for directions...\r\n\r\nPlease Note:\r\nThe admissions office can only process your application upon receipt of the proof of payment. The university is not liable for payments transferred into the wrong account or those which may not, due to bank error, reflect in Ashesi\'s bank account.'),
(2, 'online_application', 'You can apply online:\r\nClick here to open Online Application Form'),
(3, 'paper application', 'If you prefer to fill a paper application, download and complete the forms below: \r\nDownload Application Form\r\nDownload Scholarship Form\r\n'),
(4, 'application_fee', 'GHs100 for Ghanaian nationals; $50 for international applicants. '),
(5, 'application_fee_methods', 'Application Payments\r\n1. MTNMobile Money :024 526 4831\r\nRecipient: Ashesi University College\r\n\r\n Visa, Mastercard, Amex, Discover or Mobile Money (MTN, Airtel Money, Tigo Cash, Vodaphone Cash) see link below: \r\nhttps://expresspaygh.com/ashesi.\r\n\r\nDirect Deposit/Rapid Transfer at any Ecobank Branch in Ghana and West Africa\r\nAccount Name: Ashesi Admission fees\r\nAccount Number: 02000 144 116 009 05\r\nBank: Ecobank\r\nBranch: Osu\r\nCurrency: Ghana Cedi\r\nWire Transfer from within West Africa\r\n   SWIFT code: ECOCGHAC\r\nAccount Name: Ashesi University College\r\nAccount Number: 02010 144 116 009 01\r\nBank: ECOBANK, PMB CT443, ACCRA-GHANA\r\nBranch: Osu\r\nCurrency: US Dollar \r\nInternational Payments (All other countries)\r\n  SWIFT code: ECOCGHAC\r\nAccount Name: Ashesi University College\r\nAccount Number: 02010 144 116 009 01\r\nBank: ECOBANK, PMB CT443, ACCRA-GHANA\r\nBranch: Osu\r\n \r\n* Attach a copy of your payment receipt to your complete application. '),
(6, 'application_form_submission', ' Submit completed applications\r\n\r\nBy Post:\r\nAdmissions Office \r\nAshesi University College\r\nPMB CT3, Cantonments,\r\nAccra, Ghana\r\n\r\nBy E-mail\r\nScan completed application and email to: \r\nadmissions@ashesi.edu.gh\r\n\r\nIn-Person\r\nAshesi University College, \r\n1 University Avenue, \r\nBerekuso, Ghana\r\nClick here for directions...\r\n\r\nPlease Note:\r\nThe admissions office can only process your application upon receipt of the proof of payment. The university is not liable for payments transferred into the wrong account or those which may not, due to bank error, reflect in Ashesi\'s bank account. ');

-- --------------------------------------------------------

--
-- Table structure for table `ashesi_education`
--

CREATE TABLE `ashesi_education` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ashesi_education`
--

INSERT INTO `ashesi_education` (`id`, `entity`, `responses`) VALUES
(1, 'liberal_art', 'Ashesi University is a liberal art school. '),
(2, 'honour_code', 'The code is intended to build a high-trust community, to put students in charge of their ethical posture and the reputation of their alma mater'),
(3, 'class_size', 'Highest number is 60');

-- --------------------------------------------------------

--
-- Table structure for table `ashesi_location`
--

CREATE TABLE `ashesi_location` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ashesi_location`
--

INSERT INTO `ashesi_location` (`id`, `entity`, `responses`) VALUES
(1, 'ashesi_location', 'Ashesi is located in the Eastern region of Ghana, in Berekuso village'),
(3, 'ashesi_location', 'Street Address\r\n1 University Avenue, \r\nBerekuso, E/R \r\n\r\nPostal Address\r\nPMB CT3, \r\nCantonments, Accra.\r\n\r\nPhone & Email\r\n(T) +233 302 610 330 \r\n(E) info@ashesi.edu.gh');

-- --------------------------------------------------------

--
-- Table structure for table `fees`
--

CREATE TABLE `fees` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fees`
--

INSERT INTO `fees` (`id`, `entity`, `responses`) VALUES
(1, 'tuition', 'The fees listed below are per each semester, and cover instruction, textbooks, internet connectivity, and support services such as career services, health services, and counselling. \r\n\r\nTuition fee per semester 4,068 /semester\r\nOther Fees 	 	 \r\nMedical insurance (not required with proof of other medical insurance)	$240 / year\r\nOn-campus housing (optional)	$964\r\n\r\nExchange Students  	 \r\nTuition fee per course	$1,667\r\nHousing fee	$2169\r\nAdministrative fee	$1,162'),
(2, 'tuition_installment', 'Families have the option of making payments twice a semester or four times a semester, each option incurring different surcharges. \r\nFamilies who pay full tuition fees before the due date for each semester will receive an \'early payment\' discount.\r\n\r\nEarly Payment Discount 	3.5%\r\nAdditional Fees for Paying in Two Installments	3% fee\r\nAdditional Fees for Paying in four installments	6% fee'),
(3, 'tuition_exchange_student', 'Exchange Students : 	 \r\nTuition fee per course	$1,667\r\nHousing fee	$2169\r\nAdministrative fee	$1,162'),
(4, 'payment_methods', '1. Pay fees at the bank\r\nPayments within Ghana or the West Africa, deposit fees directly to any ECOBANK branch.\r\n2. Fill deposit slip\r\nComplete a deposit slip in triplicate as follows:\r\nOriginal for the bank\r\nDuplicate to be submitted to Ashesi.\r\nSubmit the Duplicate to Ashesi.\r\nKeep triplicate as evidence of payment.\r\n3. Confirm information required on the deposit slip\r\nFull name and contact number.\r\nA valid bank stamp\r\n4.Submit deposit slip to Ashesi ');

-- --------------------------------------------------------

--
-- Table structure for table `majors`
--

CREATE TABLE `majors` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `majors`
--

INSERT INTO `majors` (`id`, `entity`, `responses`) VALUES
(1, 'courses', '1. Computer Science\r\n2. Computer Engineering\r\n3. Electrical Engineering\r\n4. Mechanical Engineering\r\n5. Management Information Systems\r\n6. Business Adminstation\r\n'),
(2, 'Computer Engineering', '');

-- --------------------------------------------------------

--
-- Table structure for table `offices`
--

CREATE TABLE `offices` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `offices`
--

INSERT INTO `offices` (`id`, `entity`, `responses`) VALUES
(1, 'Dr Korsah', 'RM205-F,Engineering Building, Head of Computer Science Department'),
(2, 'Mr David Sampah', 'RM 205-E, Engineering Building, Computer Science department Lecturer'),
(3, 'Asamoah Owusu Dennis', 'RM205-E,Engineeering Building, CS Assistant Lecturer'),
(4, 'Dr Nathan Amanquah', 'RB212, Research Building, Acting Dean of Engineering '),
(5, 'Dr David Ebo Adjepon-Yamoah', 'RM205-D, Engineering Building, Assistant Lecturer '),
(6, 'DR Danyao Yiporo', 'RM205-C,Engineering Building, Lecturer,\r\nMechanical Engineering Department'),
(7, 'Faculty Interns', 'RM103,Engineering Building downstairs'),
(8, 'Adjunct Faculty', 'RM104, Engineering Building downstairs'),
(9, 'IT department', 'RM105, Engineering Building, downstairs'),
(10, 'Francis Gatsi', 'RM205-C, Engineering Building,Lecturer'),
(11, 'Kenobi Morris', 'RM 205-C, Engineering Building, Lecturer,\r\nDepartment of Mechanical Engineering'),
(12, 'Gordon Kwesi Adomdza', 'RM106,Associate Professor,\r\nBusiness Administration'),
(13, 'Mr William Annoh', 'RB111, Research Building'),
(14, 'Ms Ross Dodd', 'RB111, Research Building,Assistant Lecturer, Business Adminstration Department'),
(15, 'Dr Enyonam Kudonoo', 'RM110, Research Building, Senior Lecturer,\r\nBusiness Administration'),
(16, 'Ms Esther Laryea', 'RM110, Research Building, Adjunct Lecturer,\r\nBusiness Administration'),
(17, 'Dr Stephen Armah', 'RM112, Research Building, HOD of Business Adminstration'),
(18, 'Professor Pashington Obeng ', 'RM112, Research Building, HOD of Humanities and Social Science'),
(19, 'Mr Anthony Essel-Anderson', 'RB109, Research Building, Lecturer, Business Adminstration\r\n'),
(20, 'Mr Joseph Agyapong Mensah ', 'RB109, Research Building, Lecturer,\r\nComputer Science & Information Systems Dept'),
(21, 'Dr Ayawoa Dagbovie', 'RM108, Research Building, Department of Arts & Sciences'),
(22, 'Dr Heather Beem', 'RM108, Research Building'),
(23, 'Mr Kofi Adu-Labi', 'RB211, Research Building'),
(24, 'Mr Richard Akparibo', 'RB211, Research Building'),
(25, 'Mr Enoch Agonyo', 'RM213, Research Building'),
(26, 'Mrs Nana Ama Bortsie-Ansah', 'RM213, Research Building'),
(27, 'Elena V. Rosca', 'RM205-D, Engineering Building, Senior Lecturer'),
(29, 'Professor Angela Owusu Ansah (Provost)', 'RB214,Research Buidling, Provost'),
(31, 'Dr Kajsa Hallberg ', 'RM 111, Adminstration block'),
(32, 'Human Resource Hub', 'RM 112, Adminstration Block'),
(33, 'MDME Nathalie N\'Guessan', 'RM108 Adminstration Block, French Lecturer'),
(34, 'Mrs Kaneshia G Arhin ', 'RM108 Adminstration Block'),
(35, 'Ms Mensimah Appiah-Thompson', 'RM107, Adminstrative Block'),
(36, 'Dr Takako Mino ', 'RM107, Adminstration Block'),
(37, 'Dr Edgar Cooke', 'RM 106, Adminstrative Block, Lecturer'),
(38, 'Mr Edmund Hammah Ankomah', 'RM 106, Adminstrative Block, Lecturer'),
(39, 'Professor Benony Kwaku Gordor', 'RM105, Adminstration Block, Associate Professor'),
(40, 'Dr Leonard Baer', 'RM 105,Adminstration Block, Director of Quality Assuarance'),
(41, 'Dr Esi Ansah', 'RM104, Admistration Block, Lecturer\r\nDepartment of Business Administration'),
(42, 'Dr Sena Agyepong', 'RM104,Admistration Block, Senior Lecturer\r\nDepartment of Business Administration'),
(43, 'Dr Kwami Justina Morris', 'RM104, Adminstration Block, Lecturer,\r\nBusiness Administration Department'),
(44, 'Dr Joseph Oduro-Frimpong', 'RM103, Adminstration Block, Senior Lecturer,\r\nHumanities and Social Sciences'),
(45, 'Dr Joseph Acquah', 'RM103, Adminstrative Block'),
(46, 'Faculty Interns (Business and Humanities )', 'RM109, Adminstration Block'),
(47, 'Career Center Service', 'RM203, Adminstration Block'),
(48, 'Najeeb Mohammed', 'RM204,, Adminstration Block, Career Service Department'),
(49, 'Mrs Abigail Welbeck', 'RM204, Adminstration Block, Career Center Dpt'),
(50, 'Aunt Dee Diane Davis', 'RM205, Adminstrative Block, Director of counselling and coaching'),
(51, 'Abdul Mahdi', 'RM206, Adminstration Block, Dean of Students and Community Affairs'),
(52, 'ODIP', 'RM207, Adminstration Block, ODIP office'),
(53, 'Millicent Adjei', 'RM210, Adminstrative Block, Associate Director, Diversity and International Programs'),
(54, 'Emmanuel Ntow', 'RM211, Adminstration Block, Academic Advisor'),
(55, 'Ms Esi K Benti-Enchill', 'Counsellor and Wellness Coach'),
(56, 'Ms Frances Awua-Kyeremanten', 'Associate Director, Student Life and Engagement');

-- --------------------------------------------------------

--
-- Table structure for table `scholarships`
--

CREATE TABLE `scholarships` (
  `id` int(11) NOT NULL,
  `entity` varchar(100) NOT NULL,
  `responses` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scholarships`
--

INSERT INTO `scholarships` (`id`, `entity`, `responses`) VALUES
(1, 'scholarship_selection', 'Checks whether a student qualifies to be admitted into Ashesi, based on each applicant’s overall profile.\r\n1. The initial selection process is need-blind.\r\n\r\n2. Whether Applicants qualify to enter Ashesi.\r\n3. The Scholarship Committee, which is made up of the entire admissions team review the financial need application.\r\n4. Updates applicant on the status of their application.\r\n'),
(2, 'scholarship_covers', 'scholarship cover varies, based on demonstrated financial need. \r\nTypes of Ashesi scholarship:\r\nFull tuition scholarship\r\nPartial tuition Scholarship\r\nFull tuition + housing + living expenses\r\n\r\n*Terms and condition apply for each type of scholarship.\r\n\r\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `about_ashesi`
--
ALTER TABLE `about_ashesi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admission`
--
ALTER TABLE `admission`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `application`
--
ALTER TABLE `application`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ashesi_education`
--
ALTER TABLE `ashesi_education`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ashesi_location`
--
ALTER TABLE `ashesi_location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fees`
--
ALTER TABLE `fees`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `majors`
--
ALTER TABLE `majors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `offices`
--
ALTER TABLE `offices`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scholarships`
--
ALTER TABLE `scholarships`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `about_ashesi`
--
ALTER TABLE `about_ashesi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `admission`
--
ALTER TABLE `admission`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `application`
--
ALTER TABLE `application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `ashesi_education`
--
ALTER TABLE `ashesi_education`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `ashesi_location`
--
ALTER TABLE `ashesi_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `fees`
--
ALTER TABLE `fees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `majors`
--
ALTER TABLE `majors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `offices`
--
ALTER TABLE `offices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `scholarships`
--
ALTER TABLE `scholarships`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
