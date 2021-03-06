-- MySQL Script generated by MySQL Workbench
-- Tue Aug  8 22:37:55 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friendships
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friendships
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendships` DEFAULT CHARACTER SET utf8 ;
USE `friendships` ;

-- -----------------------------------------------------
-- Table `friendships`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendships`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table `friendships`.`friendships_again`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendships`.`friendships_again` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `users_id1` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  INDEX `fk_users_has_users_users2_idx` (`users_id1` ASC),
  INDEX `fk_users_has_users_users1_idx` (`users_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `friendships`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2`
    FOREIGN KEY (`users_id1`)
    REFERENCES `friendships`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;






