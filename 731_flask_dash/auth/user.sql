CREATE TABLE 使用者(
	user_id SERIAL PRIMARY KEY,
	姓名 VARCHAR(20),
	性別 VARCHAR(20),
	連絡電話 VARCHAR(20),
	電子郵件 VARCHAR(40),
	isGetEmail Bool,
	出生年月日 VARCHAR(20),
	自我介紹 VARCHAR(200),
	密碼 VARCHAR(100),
	連線密碼 VARCHAR(20)
);

INSERT INTO 使用者(姓名,電子郵件,密碼)
VALUES('Ian','bhbine@gmail.com','12345')

select * from 使用者

select 密碼,姓名
from 使用者
where 電子郵件='bhbine@gmail.com'