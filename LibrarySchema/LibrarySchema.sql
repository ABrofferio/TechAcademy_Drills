IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Book' AND xtype='U')
CREATE TABLE Book
(
BookID int IDENTITY (1,1) NOT NULL PRIMARY KEY,
Title nvarchar(50) NOT NULL,
PubName nvarchar(50) NOT NULL,
)
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Authors' AND xtype='U')
CREATE TABLE Authors
(
BookID int IDENTITY(1,1) NOT NULL Primary Key,
AuthorName nvarchar (50) NOT NULL,
)
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Publisher' AND xtype='U')
CREATE TABLE Publisher
(
PubID int IDENTITY(1,1) NOT NULL Primary Key,
PubName nvarchar(50) Not Null,
PubAddress nvarchar(50) Null,
PubPhone int Null,
)
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Copies' AND xtype='U')
CREATE TABLE Copies
(
CopyID int IDENTITY(1,1) not null,
BookID int not null,
BranchID int not null,
NumCopies int not null
)
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Loans' AND xtype='U')
CREATE TABLE Loans
(
CopyID int not null,
BookID int not null,
BranchID int not null,
CardNo int not null,
DateOut nvarchar(50) null,
DueDate nvarchar(50) null
)
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Branch' AND xtype='U')
CREATE TABLE Branch
(
BranchID int IDENTITY(1,1) not null  primary key,
BranchName nvarchar(50) not null,
BranchAddress nvarchar(50) null
)
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Borrower' AND xtype='U')
CREATE TABLE Borrower
(
CardNo int IDENTITY(1,1) not null,
BorrowerName nvarchar(50) not null,
BorrowerAddress nvarchar(50) null,
BorrowerPhone int null,
)


Insert Into Book
(Title, PubName)
Values 
('Harry Potter One', 'Penguin Books'),
('Harry Potter Two', 'Penguin Books'),
('Harry Potter Three', 'Penguin Books'),
('Harry Potter Four', 'Penguin Books'),
('Harry Potter Five', 'Penguin Books'),
('Harry Potter Six', 'Penguin Books'),
('Harry Potter Seven', 'Penguin Books'),
('The Lord of the Rings One', 'Columbia'),
('The Lord of the Rings Two', 'Columbia'),
('The Lord of the Rings Three', 'Columbia'),
('The Hobbit', 'Columbia'),
('The Count of Monte Cristo', 'Random House'),
('A Song of Ice and Fire series', 'Pearson'),
('To Kill a Mockingbird', 'Harper Collins'),
('The Lost Tribe', 'Harper Collins'),
('The Little Prince', 'Hachette Livre'),
('It', 'Simon & Schuster'),
('Siddhartha', 'Pearson'),
('Candide', 'Random House'),
('The Girl with the Dragon Tattoo', 'Random House'),
('The Alchemist', 'Simon & Schuster');

Insert Into Authors
(AuthorName)
Values
('J.K. Rowling'),
('J.K. Rowling'),
('J.K. Rowling'),
('J.K. Rowling'),
('J.K. Rowling'),
('J.K. Rowling'),
('J.K. Rowling'),
('J.R.R. Tolkien'),
('J.R.R. Tolkien'),
('J.R.R. Tolkien'),
('J.R.R. Tolkien'),
('Alexandre Dumas'),
('George R.R. Martin'),
('Harper Lee'),
('Iam Anauthor'),
('Antoine de Saint-Exupery'),
('Stephen King'),
('Herman Hesse'),
('Voltaire'),
('Stieg Larsson'),
('Paulo Coelho');

Insert Into Publisher
(PubName)
Values 
('Penguin Books'),
('Columbia'),
('Random House'),
('Pearson'),
('Harper Collins'),
('Hachette Livre'),
('Simon & Schuster');

Insert Into Copies
(BookID, BranchID, NumCopies)
Values 
(1, 1, 2 ),
(1, 1, 2 ),
(1, 2, 2 ),
(1, 2, 2 ),
(1, 3, 2 ),
(1, 3, 2 ),
(1, 4, 2 ),
(1, 4, 2 ),
(2, 1, 2 ),
(2, 1, 2 ),
(2, 2, 2 ),
(2, 2, 2 ),
(2, 3, 2 ),
(2, 3, 2 ),
(2, 4, 2 ),
(2, 4, 2 ),
(3, 1, 2 ),
(3, 1, 2 ),
(3, 2, 2 ),
(3, 2, 2 ),
(3, 3, 2 ),
(3, 3, 2 ),
(3, 4, 2 ),
(3, 4, 2 ),
(4, 1, 2 ),
(4, 1, 2 ),
(4, 2, 2 ),
(4, 2, 2 ),
(4, 3, 2 ),
(4, 3, 2 ),
(4, 4, 2 ),
(4, 4, 2 ),
(5, 1, 2 ),
(5, 1, 2 ),
(5, 2, 2 ),
(5, 2, 2 ),
(5, 3, 2 ),
(5, 3, 2 ),
(5, 4, 2 ),
(5, 4, 2 ),
(6, 1, 2 ),
(6, 1, 2 ),
(6, 2, 2 ),
(6, 2, 2 ),
(6, 3, 2 ),
(6, 3, 2 ),
(6, 4, 2 ),
(6, 4, 2 ),
(7, 1, 2 ),
(7, 1, 2 ),
(7, 2, 2 ),
(7, 2, 2 ),
(7, 3, 2 ),
(7, 3, 2 ),
(7, 4, 2 ),
(7, 4, 2 ),
(8, 1, 2 ),
(8, 1, 2 ),
(8, 2, 2 ),
(8, 2, 2 ),
(9, 3, 2 ),
(9, 3, 2 ),
(9, 4, 2 ),
(9, 4, 2 ),
(10, 1, 2 ),
(10, 1, 2 ),
(10, 2, 2 ),
(10, 2, 2 ),
(11, 3, 2 ),
(11, 3, 2 ),
(11, 4, 2 ),
(11, 4, 2 ),
(12, 1, 2 ),
(12, 1, 2 ),
(12, 2, 2 ),
(12, 2, 2 ),
(12, 3, 2 ),
(12, 3, 2 ),
(12, 4, 2 ),
(12, 4, 2 ),
(13, 1, 2 ),
(13, 1, 2 ),
(13, 2, 2 ),
(13, 2, 2 ),
(14, 3, 2 ),
(14, 3, 2 ),
(14, 4, 2 ),
(14, 4, 2 ),
(15, 2, 2 ),
(15, 2, 2 ),
(15, 4, 2 ),
(15, 4, 2 ),
(16, 1, 2 ),
(16, 1, 2 ),
(16, 2, 2 ),
(16, 2, 2 ),
(16, 3, 2 ),
(16, 3, 2 ),
(16, 4, 2 ),
(16, 4, 2 ),
(17, 1, 2 ),
(17, 1, 2 ),
(17, 3, 2 ),
(17, 3, 2 ),
(18, 3, 2 ),
(18, 3, 2 ),
(18, 4, 2 ),
(18, 4, 2 ),
(19, 3, 2 ),
(19, 3, 2 ),
(19, 4, 2 ),
(19, 4, 2 ),
(20, 1, 2 ),
(20, 1, 2 ),
(20, 2, 2 ),
(20, 2, 2 ),
(21, 1, 2 ),
(21, 1, 2 ),
(21, 2, 2 ),
(21, 2, 2 ),
(21, 3, 2 ),
(21, 3, 2 ),
(21, 4, 2 ),
(21, 4, 2 );

Insert Into Loans
(CopyID, BookID, BranchID, CardNo, DateOut, DueDate)
Values 
(1, 1, 1, 1, '1/12/16', '8/15/16'),
(3, 1, 2, 2, '6/15/16', '9/25/16'),
(11, 2, 2, 2, '6/15/16', '9/25/16'),
(19, 3, 2, 2, '6/15/16', '9/25/16'),
(27, 4, 2, 2, '1/12/16', '8/15/16'),
(35, 5, 2, 2, '6/15/16', '9/25/16'),
(5, 1, 3, 3, '1/12/16', '8/15/16'),
(61, 9, 3, 3, '6/15/16', '9/25/16'),
(69, 11, 3, 3, '1/12/16', '8/15/16'),
(77, 12, 3, 3, '6/15/16', '9/25/16'),
(85, 14, 3, 3, '1/12/16', '8/15/16'),
(2, 1, 1, 4, '6/15/16', '9/25/16'),
(7, 1, 4, 5, '6/15/16', '9/25/16'),
(8, 1, 4, 6, '1/12/16', '8/15/16'),
(9, 2, 1, 7, '1/12/16', '8/15/16'),
(10, 2, 1, 8, '6/15/16', '9/25/16');

Insert Into Branch
(BranchName, BranchAddress)
Values
('Downtown', '334 Jean St'),
('Sharpstown', '1234 Tom St'),
('Central', '555 Jane St.'),
('Uptown', '999 Bob St');

Insert Into Borrower
(BorrowerName, BorrowerAddress)
Values
('Jane Tom', '324 A St'),
('Bill Bob', '1434 B St'),
('Hank Smith', '535 C St.'),
('Gerry Gory', '969 D St'),
('Linda Tom', '3364 E St'),
('John James', '1734 F St'),
('Tina Tammy', '85 G St'),
('Belinda Thomas', 'H  St'),
('Sally Sue', '433 Smith St'),
('James Johnson', '987 Hope Ave');