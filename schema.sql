drop table if exists ideas;
create table ideas(
id integer primary key autoincrement,
creator_name text not null,
creator_role text not null,
project_name text not null,
project_desc text not null,
tags text,
spots int,
position_one text,
position_one_owner text,
position_two text,
position_two_owner text
);