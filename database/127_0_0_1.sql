-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Дек 19 2024 г., 17:25
-- Версия сервера: 10.4.32-MariaDB
-- Версия PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `christmas`
--
CREATE DATABASE IF NOT EXISTS `christmas` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `christmas`;

-- --------------------------------------------------------

--
-- Структура таблицы `greetings`
--

CREATE TABLE `greetings` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `text` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `greetings`
--

INSERT INTO `greetings` (`id`, `text`) VALUES
(1, 'Пусть этот Новый год принесет тебе море радости, горсть подарков и целую кучу счастливых мгновений!'),
(2, 'С Новым годом! Желаю тебе свершений, вдохновения и незабываемых моментов, которые запомнятся надолго.'),
(3, 'Пусть Новый год откроет новые горизонты и принесет тебе удачу, как снежинка, падающая в лучах новогоднего света.'),
(4, 'С наступающим Новым годом! Желаю тебе тепла, света и доброты в твоём сердце.'),
(5, 'Новый год – это время чудес! Пусть твои мечты сбудутся, как самые яркие новогодние огни.'),
(6, 'Пусть новогодняя ночь окутает тебя волшебством, а утро встретит тебя с улыбкой судьбы.'),
(7, 'Желаю тебе Нового года, наполненного счастьем и радостью, словно щедрый подарок под ёлкой.'),
(8, 'С Новым годом, дорогой! Пусть этот год будет лучше предыдущего, и принесёт тебе невероятные эмоции!'),
(9, 'Пусть Новый год подарит тебе все, о чём ты мечтаешь, а также много смеха и позитивных впечатлений.'),
(10, 'Пусть этот Новый год станет началом новой прекрасной истории, полной любви и счастья.'),
(11, 'Зажги новогодние огни внутри себя, и пусть они освещают путь к твоим мечтам.'),
(12, 'Пусть Новый год откроет двери к новым возможностям и наполнит твою жизнь радостью.'),
(13, 'Желаю тебе Нового года, наполненного волшебством и неповторимой атмосферой праздника.'),
(14, 'С Новым годом! Пусть этот год будет полон ярких красок и незабываемых воспоминаний.'),
(15, 'Новый год – это время надежд и желаний! Пусть твои мечты сбудутся, как новогодняя сказка.'),
(16, 'Пусть Новый год подарит тебе волшебство, радость и бесконечное счастье.'),
(17, 'С наступающим Новым годом! Желаю тебе крепкого здоровья, удачи и невероятного счастья.'),
(18, 'Пусть этот Новый год будет наполнен любовью, счастьем и волшебством, как новогодняя ночь.'),
(19, 'Новый год – это возможность начать всё с чистого листа! Желаю тебе вдохновения и новых достижений.'),
(20, 'Пусть Новый год принесёт тебе радость, как новогодние фейерверки, озаряющие ночное небо.'),
(21, 'С Новым годом! Желаю, чтобы этот год был полон ярких впечатлений и незабываемых событий.'),
(22, 'Пусть этот Новый год станет для тебя годом процветания, гармонии и исполненных желаний.'),
(23, 'Желаю тебе новогодней ночи, полной чудес, и нового года, наполненного счастьем.'),
(24, 'Пусть в Новом году тебя сопровождают радость, успех и вдохновение, словно яркие новогодние огни.'),
(25, 'С Новым годом! Желаю, чтобы твой год был полон любви, смеха и незабываемых моментов.'),
(26, 'Новый год – это время для новых начинаний! Желаю тебе всего самого лучшего и яркого.'),
(27, 'Пусть новогодняя ночь окутает тебя волшебством, а Новый год принесёт тебе исполнение желаний.'),
(28, 'Желаю тебе Нового года, наполненного теплом, заботой и искренними чувствами.'),
(29, 'С Новым годом! Пусть этот год будет полон новых открытий и свершений.'),
(30, 'Пусть Новый год принесет тебе всё самое лучшее, о чём ты только мечтаешь!');

-- --------------------------------------------------------

--
-- Структура таблицы `greetings_for_friend`
--

CREATE TABLE `greetings_for_friend` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `id_tg_recipient` bigint(20) NOT NULL,
  `greeting` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_tg` bigint(20) NOT NULL,
  `username` text NOT NULL,
  `send_greetings` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `greetings`
--
ALTER TABLE `greetings`
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `greetings_for_friend`
--
ALTER TABLE `greetings_for_friend`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_user` (`id_user`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `greetings`
--
ALTER TABLE `greetings`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT для таблицы `greetings_for_friend`
--
ALTER TABLE `greetings_for_friend`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `greetings_for_friend`
--
ALTER TABLE `greetings_for_friend`
  ADD CONSTRAINT `greetings_for_friend_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
