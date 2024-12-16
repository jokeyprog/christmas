-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Дек 16 2024 г., 19:57
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
(1, 'С Новым годом! Пусть этот праздник принесёт радость и волшебство в Вашу жизнь.'),
(2, 'С Новым годом! Желаю Вам, незабываемых приключений в Новом году, пусть сбываются все Ваши мечты и желания.'),
(3, 'Поздравляю с Праздником! Пусть Новый год станет началом новой главы в Вашей жизни, полной счастья, успеха и любви.'),
(4, 'Поздравляю Вас с Новым годом! Наслаждайтесь каждым моментом этого праздника и верьте в чудеса, которые обязательно случатся.'),
(5, 'Ура! Поздравляю! Пусть в Новом году Вас окружают только добрые люди и приятные сюрпризы'),
(6, 'С Новым годом! От всей души желаю Вам исполнения всех желаний в новогоднюю ночь.'),
(7, 'Пусть этот праздник подарит Вам незабываемые эмоции и воспоминания.'),
(8, 'С Новым годом! Пусть этот год будет полон радости, веселья и приятных сюрпризов.'),
(9, 'Счастливого Нового года! Пусть в Вашем доме всегда царят уют, тепло и любовь, а в сердце — счастье и гармония.'),
(10, 'Наслаждайтесь каждой минутой этого праздника и верьте в чудеса, которые обязательно произойдут.'),
(11, 'Пусть в Новом году Ваша жизнь наполнится яркими красками, а удача будет сопутствовать во всём.'),
(12, 'С праздником! Пусть этот Новый год станет началом новой прекрасной эры в Вашей жизни.'),
(13, 'С Новым годом! Пусть в Вашем сердце всегда звучит музыка радости и счастья, а душа будет полна надежд и веры в лучшее.'),
(14, 'Пусть в Новом году Ваша жизнь будет наполнена любовью, успехом и благополучием.'),
(15, 'С Новым годом! Пусть этот праздник подарит Вам незабываемые впечатления и зарядит позитивом на весь год.'),
(16, 'Счастливого Нового года! Пусть в Вашм доме всегда царит атмосфера уюта, тепла и взаимопонимания, а сердца будут полны любви и добра.');

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
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

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
