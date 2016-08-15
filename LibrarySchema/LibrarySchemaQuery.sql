SELECT Count(Copies.CopyID)
FROM Book
INNER JOIN Copies
ON Book.BookID=Copies.BookID
INNER JOIN Branch
ON Copies.BranchID=Branch.BranchID
WHERE BranchName='Sharpstown' AND Book.Title='The Lost Tribe';

SELECT Branch.BranchName, Count(Copies.CopyID)
FROM Book
INNER JOIN Copies
ON Book.BookID=Copies.BookID
INNER JOIN Branch
ON Copies.BranchID=Branch.BranchID
WHERE Book.Title='The Lost Tribe'
GROUP BY Branch.BranchName;

SELECT Borrower.BorrowerName, Borrower.CardNo, Loans.CopyID, Loans.BookID
FROM Borrower
LEFT OUTER JOIN Loans
ON Borrower.CardNo=Loans.CardNo;

SELECT Book.Title, Borrower.BorrowerName, Borrower.BorrowerAddress
FROM Borrower
INNER JOIN Loans
ON Borrower.CardNo=Loans.CardNo
INNER JOIN Branch
ON Loans.BranchID=Branch.BranchID
INNER JOIN Book
ON Book.BookID = Loans.BookID
WHERE Branch.BranchName='Sharpstown' AND Loans.DueDate='8/15/16';

SELECT Branch.BranchName, Count(Loans.CopyID)
FROM Loans
INNER JOIN Branch
ON Loans.BranchId=Branch.BranchID
GROUP BY Branch.BranchName;

SELECT Borrower.BorrowerName, Borrower.BorrowerAddress, Count(Loans.CopyID)
FROM Loans
INNER JOIN Borrower
ON Loans.CardNo=Borrower.CardNo
GROUP BY Borrower.BorrowerName, Borrower.BorrowerAddress
HAVING Count(Loans.CopyID)>5;

SELECT Book.Title, Count(Copies.CopyID)
FROM Book
INNER JOIN Copies
ON Book.BookID=Copies.BookID
INNER JOIN Authors
ON Book.BookID = Authors.BookID
INNER JOIN Branch
ON Copies.BranchID=Branch.BranchID
WHERE Branch.BranchName='Central' AND Authors.AuthorName ='Stephen King'
GROUP BY Book.Title;