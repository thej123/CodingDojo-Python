-- MySQL Script generated by MySQL Workbench
-- Thu Aug 10 17:39:30 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema LoRegdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LoRegdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LoRegdb` DEFAULT CHARACTER SET utf8 ;
USE `LoRegdb` ;

-- -----------------------------------------------------
-- Table `LoRegdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LoRegdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;