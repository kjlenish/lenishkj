use db;

create table students
(
id int primary key auto_increment,
sname varchar(25),
age int,
gender varchar(10)
);

insert into students (id, sname, age, gender) values (1, 'sasi', 19, 'male');
insert into students (id, sname, age, gender) values (2, 'janu', 29, 'female');
insert into students (id, sname, age, gender) values (3, 'ambu', 20, 'male');

select * from students;

update students set sname = 'janet' where id= 2;
delete from students where id = 3;

select * from students;