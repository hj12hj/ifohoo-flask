create table dynamic_report
(
    form_code            varchar(30) not null comment '表单代码 主键'
        primary key,
    form_name            varchar(60) not null comment '表单名称',
    form_default_content text        not null comment '表单默认内容',
    form_detail_content  text        null comment '表单详情内容',
    version              int         not null comment '版本号',
    creator              bigint      not null comment '创建人',
    create_time          datetime    not null comment '创建时间',
    update_by            bigint      null comment '修改人',
    update_time          datetime    null comment '修改时间'
)
    comment '表单信息表' charset = utf8;

create table dynamic_report_history
(
    template_id          varchar(64) not null comment '主键'
        primary key,
    form_code            varchar(30) not null comment '表单代码',
    form_default_content text        not null comment '表单默认内容',
    form_detail_content  text        null comment '表单详情内容',
    history_time         datetime    not null comment '历史版本时间',
    form_version         int         not null comment '表单版本',
    last_flag            varchar(1)  not null comment '是否最新版本',
    version              int         not null comment '版本号',
    creator              bigint      not null comment '创建人',
    create_time          datetime    not null comment '创建时间',
    update_by            bigint      null comment '修改人',
    update_time          datetime    null comment '修改时间'
)
    comment '历史表' charset = utf8;

