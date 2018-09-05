-- #######################################
-- Purpose: 
--	- DDL for the Unbabel Challenge
--
-- Author:
-- 	Bee-Engineering
-- 
-- #######################################

CREATE TABLE TRANSLATION(
		ID SERIAL PRIMARY KEY NOT NULL,
		TRANS_UID VARCHAR(1024) NULL,
		SRC_LANG VARCHAR(10) DEFAULT 'EN' NOT NULL,
		TRG_LANG VARCHAR(10)  DEFAULT 'ES' NOT NULL,
		TXT VARCHAR(4048) NOT NULL,
		TRANS_RESULT VARCHAR(4048) NULL,
		STATE VARCHAR(50) DEFAULT 'new'
);

