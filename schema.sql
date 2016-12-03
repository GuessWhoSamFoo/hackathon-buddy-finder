drop table if exists ideas;
create table ideas(
id integer primary key autoincrement,
author text not null,
title text not null,
description text not null,
teammates text,
current_num int,
max_num int
);