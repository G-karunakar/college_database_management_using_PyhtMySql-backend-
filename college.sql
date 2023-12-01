
-- createing database

create database record_maintaince;
use record_maintaince;

-- creating tables

create table student (s_id int(10) auto_increment primary key,s_name varchar(30),age int(2),d_id int(10),duretion varchar(10));
create table deportment (d_id int(10) auto_increment primary key,d_name varchar(30),hod varchar (30));
create table faculty(f_id int(10) auto_increment primary key,f_name varchar(30),age int(2),d_id int(10),designetion varchar(10));
create table fee(s_id int(10) auto_increment primary key,fee int,paid int,status varchar(10))

-- tables details

SHOW tables;
describe student;
describe deportment;
describe faculty;
describe fee;

-- enter data into deportment

INSERT INTO deportment  VALUES ('990000001', 'mca', 'kiran');
INSERT INTO deportment (`d_name`, `hod`) VALUES ('mba', 'vamsi');
INSERT INTO deportment (`d_name`, `hod`) VALUES ('msc(cs)', 'narayana');
INSERT INTO deportment (`d_name`, `hod`) VALUES ('msc(ch)', 'sharath');
INSERT INTO deportment (`d_name`, `hod`) VALUES ('msc(bi)', 'renu');
INSERT INTO deportment (`d_name`, `hod`) VALUES ('ma', 'mamatha');
INSERT INTO deportment (`d_name`, `hod`) VALUES ('mcom', 'mabuni');


-- enter data into faculty

INSERT INTO faculty VALUES ('880000001', 'kiran', '32', '990000001', 'profecor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('madhan', '34', '990000002', 'professor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('madhav', '43', '990000003', 'hod');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('ravi', '52', '990000004', 'assistent professor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('mamatha', '43', '990000005', 'hod');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('narayana', '47', '990000006', 'professor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('surya', '39', '990000007', 'assistent professor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('siva', '50', '990000003', 'hod');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('kumar', '35', '990000002', 'assistent professor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('naveen', '42', '990000005', 'assistent professor');
INSERT INTO faculty (`f_name`, `age`, `d_id`, `designetion`) VALUES ('renu', '65', '990000001', 'professor');

-- enter data into student

INSERT INTO `record_maintaince`.`student` (`s_id`, `s_name`, `age`, `d_id`, `duretion`) VALUES ('770000001', 'karunakar', '23', '990000001', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('madhan', '22', '990000002', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('leeka', '27', '990000003', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('kavitha', '24', '990000004', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('kalavathi', '22', '990000005', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('pavan', '22', '990000006', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('naveen', '23', '990000007', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('bala', '22', '990000004', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('venki', '23', '990000001', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('venkatadhri', '23', '990000002', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('sandheep', '24', '990000003', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('kora', '23', '990000005', '2021-23');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('kudhire', '24', '990000006', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('dhileep', '23', '990000007', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('jaggu', '23', '990000002', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('manohar', '23', '990000005', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('rajesh', '22', '990000006', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('suresh', '24', '990000002', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('achusma', '25', '990000001', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('joshna', '23', '990000005', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('rukku', '21', '990000003', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('ragini', '22', '990000004', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('padmavathi', '23', '990000007', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('anusha', '23', '990000003', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('mounika', '22', '990000002', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('dhevi', '24', '990000006', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('navya', '24', '990000002', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('manju', '24', '990000004', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('krishna', '25', '990000001', '2022-24');
INSERT INTO `record_maintaince`.`student` (`s_name`, `age`, `d_id`, `duretion`) VALUES ('manisha', '21', '990000005', '2022-24');

--  enter data into fee

INSERT INTO fee VALUES ('770000001', 100000, 100000, 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '0', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '0', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '0', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '0', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '50000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '0', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '0', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '80000', 'no');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '100000', 'yes');
INSERT INTO `record_maintaince`.`fee` (`fee`, `paid`, `status`) VALUES ('100000', '80000', 'no');

-- assigning keys

alter table student add foreign key(s_id) references fee(s_id);
alter table student add foreign key(d_id) references deportment(d_id);
alter table faculty add foreign key(d_id) references deportment(d_id);
