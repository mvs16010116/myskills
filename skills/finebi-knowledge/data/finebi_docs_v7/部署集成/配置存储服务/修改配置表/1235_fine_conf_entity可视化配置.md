---
title: fine_conf_entity可视化配置
doc_id: 1235
url: https://help.fanruan.com/finebi/doc-view-1235.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:26
version: "7.X"
---

> 1.&nbsp;概述1.1&nbsp;版本FineBI服务器版本fine_conf_entity可视化配置插件功能变更7.0V1.9.36-1.2 应用场景在FineBI系统中，有部分配置信息没有前端配

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# fine_conf_entity可视化配置
[__](<doc-edit-1235.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[61](<edition-list-1235.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-06-03 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| fine_conf_entity可视化配置插件| 功能变更  
  
---|---|---  
7.0| V1.9.36| -  
### 1.2 应用场景
在FineBI系统中，有部分配置信息没有前端配置界面，这些信息仅存储在finedb配置库的fine_conf_entity表中。
管理员只能通过直接修改表字段值来进行更改。然而，finedb配置库是整个FineBI系统运行的基础配置库，任何误操作或人为损坏都可能导致不可修复的bug。
如何确保管理员能够安全、便捷地修改fine_conf_entity表中的配置信息，避免误操作带来的风险？
### 1.3 功能简介
为了解决这一问题，帆软提供了「fine_conf_entity可视化配置」插件。
该插件帮助管理员通过可视化界面安全地修改相关配置，降低误操作的风险，确保系统的稳定运行。
注：FineDB 配置库用于存放工程配置信息，各表之间存在关联关系，随意改动可能导致工程无法启动等严重后果。
如需使用该插件以外的方法修改 finedb 数据库内容，请与帆软技术支持确认后再进行操作。
请勿随意手动增！删！改！finedb 数据库内的任何数据！有可能造成不可修复的 BUG，需自行承担后果。
## 2\. 示例
### 2.1 插件安装
点击下载插件：[fine_conf_entity可视化配置插件](<https://market.fanruan.com/plugin/1052a471-0239-4cd8-b832-045d53182c5d>)
插件安装方法请参照：[插件管理](<https://help.fanruan.com/finebi7.0/doc-view-459.html>)
### 2.2 系统工具
插件安装成功后，超级管理员登录 FineBI 系统，点击「管理系统」，新增「系统工具」设置。如下图所示：
注：由于 FineDB 的修改非常重要，影响较大，因此仅支持超管进行操作，不支持次级管理员操作。
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 参数配置
配置方法支持以下两种：  

  * **选择参数配置：** 系统参数名（key）下拉框中罗列了支持配置的 fine_conf_entity 参数，用户可直接在下拉框中选择参数，配置参数值（value）。
  * **自定义参数配置：** 用户可自行输入支持配置的 fine_conf_entity 参数名（key），并自动跳出参数值（value），用户可修改并保存参数值。


两种配置方式支持配置的参数完全相同，可修改的 fine_conf_entity 中的配置参数和参数值如下表所示：
参数名  
| 参数描述| 参数值  
---|---|---  
AttachmentStrategyConfig.localPrefer| 临时资源附件优先存储在本地| 参数值需为布尔型，默认为truefalse：临时资源优先存储在文件服务器true：临时资源优先存储在工程节点本地  
BIUpdateConfig.autoBackup| BI自动备份| 参数值需为布尔型，默认为falsefalse：BI不自动备份true：BI自动备份  
BackupConfig.customKeyLength| 备份conf表，自定义id长度| 参数值需为正整型默认值为1500  
BackupConfig.customValueLength| 备份conf表，自定义value长度| 参数值需为正整型默认值为65536  
CacheConfig.maxMemSize| 共享数据集缓存空间上限| 参数值需为非负整型默认值为4194304  
CloudFeatureConfig.recordFineMarkId| 固化埋点回传| 参数值需为布尔型，默认为truefalse：固化埋点不回传true：固化埋点回传  
CloudFeatureConfig.sendSolidByJsonp| 通过浏览器获取服务器运行数据| 参数值需为布尔型，默认为truefalse：通过浏览器无法获取服务器运行数据true：通过浏览器获取服务器运行数据  
CloudFeatureConfig.shellExecute| 通过shell命令获取服务器配置信息| 参数值需为布尔型，默认为truefalse：通过shell命令无法获取服务器配置信息true：通过shell命令获取服务器配置信息  
CloudFeatureConfig.uploadFileByMarket| 通过帆软市场上传服务器运行数据| 参数值需为布尔型，默认为falsefalse：不通过帆软市场上传服务器运行数据true：通过帆软市场上传服务器运行数据  
ClusterRedirectConfig.enableSessionIDGenerationStrategy| 是否启用集群下的sessionID生成策略| 参数值需为布尔型，默认为falsefalse：不启用集群下的sessionID生成策略true：集群下的sessionID的尾部会拼接上集群的nodeID  
ClusterTimeMonitorConfig.permitCount| 集群单次时间误差检测任务中, 多次误差分析中最小成功次数| 参数值需为正整型默认值为1  
ClusterTimeMonitorConfig.permitError| 集群单次时间误差检测任务中,，允许时间误差值，单位ms| 参数值需为正长整型默认值为10000  
ClusterTimeMonitorConfig.sumCount| 集群单次时间误差检测任务中, 尝试误差分析的总次数| 参数值需为正整型默认值为3  
CookieConfig.forceSameSite| cookie强制添加SameSite=None| 参数值需为布尔型，默认为falsefalse：cookie不添加SameSite=Nonetrue：cookie强制添加SameSite=None  
CronUpdateConfig.typeMap.plugins| 插件自动更新的定时更新是否开启| 如需关闭工程启动后每晚11点的外网更新插件，请将参数值修改为false，否则无需改动  
CustomConfig.absPositionOfFloat| 悬浮元素是否以绝对位置展示（不受单元格扩展的影响）| 参数值需为布尔型，默认为falsefalse：不以绝对位置展示（不受单元格扩展的影响）  
true：以绝对位置展示（受单元格扩展的影响）  
CustomConfig.columnMatchRuleForWidgetValue| 数据字段是否区分大小写| 参数值如下，默认为case_ignorecase_ignore：不区分大小写  
case_sensitive：区分大小写  
CustomConfig.dataTransType| 定义填报提交,校验请求中前端模板数据的传输形式| 参数值如下，默认为xmlxml：以xml字符串格式传输json：以json字符串格式传输  
CustomConfig.excelAdjustHeight| Excel导出行高系数| 参数值需为非负单精度浮点型默认值为20.1  
CustomConfig.excelAdjustWidth| Excel导出列宽系数| 参数值需为非负单精度浮点型默认值为34.742  
CustomConfig.exportFullImg4Excel| Excel导出的时候是否导出完整图片| 参数值需为布尔型，默认为falsefalse：Excel导出时，不导出完整图片true：Excel导出时，导出完整图片  
CustomConfig.printWidget| 是否导出/打印控件(目前支持打印复选框与复选框组控件)| 参数值需为布尔型，默认为falsefalse：不导出/打印控件true：导出/打印控件  
CustomConfig.screenScaleEnabled| 控制设计器缩放| 参数值需为布尔型，默认为true  
false：关闭设计器缩放true：开启设计器缩放  
CustomConfig.wordAdjustHeight| Word导出用于调整行高的数值，防止内容高度在某些临界值时出现空白页| 参数值需为非负整型默认值为2  
DatacenterOptimizationConfig.maxAccelerateCacheColumns| 关联缓存更新的最大列数限制| 参数值需为正整数，默认为 200关联缓存的总列数超过 200 列，会加速失败  
DelayUpdateConfig.delaySwitchMap.plugins| 插件自动更新的延迟更新是否开启| 如需关闭工程启动后延迟一段时间的插件自动更新，请将参数值修改为false，否则无需改动  
  
DingTalkConfig.checkRedirectDomainEnable| 开启或关闭钉钉插件单点登录域名一致性校验| 参数值为布尔型，默认为truetrue：开启钉钉插件单点登录域名一致性校验false：关闭钉钉插件单点登录域名一致性校验  
DingTalkConfig.requestConfigEnable| 开启或关闭钉钉插件高级请求配置| 参数值需为布尔型，默认为falsefalse：关闭钉钉插件高级请求配置true：开启钉钉插件高级请求配置  
DistributedOptimizationConfig.spiderConfig.local_file_delete_retry_mode| 本地文件删除重试机制| 参数值需为布尔型，默认为truetrue：本地文件删除重试机制false：本地文件不删除重试机制  
DistributedOptimizationConfig.spiderConfig.local_file_delete_retry_period| 本地文件删除重试周期| 参数值需为正整数，默认为10  
DistributedOptimizationConfig.spiderConfig.local_file_delete_retry_time| 本地文件删除重试次数| 参数值需为正整数，默认为3  
DistributedOptimizationConfig.spiderConfig.max_slice_memory_size| slice最大内存设置| 参数值需为正整数，默认为52428800  
DistributedOptimizationConfig.spiderConfig.spark_blockManager_port| spark blockManager端口| 参数值需为[1001, 65535]区间内的正整数默认值为17778  
DistributedOptimizationConfig.spiderConfig.spark_driver_host| spark driver主机名| 参数值需为字符串，默认为空  
  
DistributedOptimizationConfig.spiderConfig.spark_driver_maxResultSize| spark返回driver端最大结果集大小| 参数值需为字符串，默认为1g  
DistributedOptimizationConfig.spiderConfig.spark_driver_port| spark driver端口| 参数值需为[1001, 65535]区间内的正整数默认值为17777  
DistributedOptimizationConfig.spiderConfig.spark_executor_cores| spark executor核心| 参数值需为正整数，默认为12  
DistributedOptimizationConfig.spiderConfig.spark_executor_memory| spark executor内存| 参数值需为字符串，默认为6g  
DistributedOptimizationConfig.spiderConfig.spark_local_dir| spark临时文件目录，计算吐磁盘目录| 参数值需为字符串，默认为空  
DistributedOptimizationConfig.spiderConfig.spark_master_host| spark master主机名| 参数值需为字符串，默认为空  
DistributedOptimizationConfig.spiderConfig.spark_master_port| spark master端口| 参数值需为[1001, 65535]区间内的正整数默认值为7077  
DistributedOptimizationConfig.spiderConfig.spark_memory_fraction| spark占用jvm内存比例| 参数值需为0~1的正整数，默认值为0.3spark占用太多的jvm内存可能会导致宕机  
DistributedOptimizationConfig.spiderConfig.spark_scheduler_allocation_file| spark调度分配文件| 参数值需为字符串，默认为空  
DistributedOptimizationConfig.spiderConfig.spark_scheduler_mode| spark调度模式| 参数值需为字符串，默认为CAPACITY  
DistributedOptimizationConfig.spiderConfig.spark_shuffle_service_enabled| shuffle过程数据外排| 参数值需为布尔型，默认为truetrue：shuffle过程数据外排false：shuffle过程数据不外排  
DistributedOptimizationConfig.spiderConfig.spark_sql_adaptive_advisoryPartitionSizeInBytes| 计算自适应目标块大小| 参数值需为字符串，默认值为200M  
DistributedOptimizationConfig.spiderConfig.spark_sql_adaptive_coalescePartitions_minPartitionNum| 最小数据块，按照默认200M为1块分| 参数值需为正整数，默认值为1  
DistributedOptimizationConfig.spiderConfig.spark_sql_adaptive_enabled| 计算自适应功能| 参数值需为布尔型，默认为truetrue：计算自适应功能false：不计算自适应功能  
DistributedOptimizationConfig.spiderConfig.spark_sql_autoBroadcastJoinThreshold| spark broadcastjoin读取过多导致oom，设为-1采用sortjoin规避掉| 默认值为-1spark broadcastjoin读取过多可能导致oom，设为-1可采用sortjoin规避  
DistributedOptimizationConfig.spiderConfig.spark_sql_broadcastTimeout| broadcast的超时时间| 参数值需为字符串，默认为12000  
DistributedOptimizationConfig.spiderConfig.spark_sql_shuffle_partitions| spark shuffle的并发块数| 参数值需为字符串，默认为空  
DistributedOptimizationConfig.spiderConfig.spark_sql_sortMergeJoinExec_buffer_in_memory_threshold| sortMergeJoin算子内存最大数据量| 参数值需为字符串，默认为100000  
DistributedOptimizationConfig.spiderConfig.spark_sql_sortMergeJoinExec_buffer_spill_threshold| sortMergeJoin算子吞吐阈值| 参数值需为字符串，默认为100000  
DistributedOptimizationConfig.spiderConfig.spark_ui_port| 设置spark的web页面访问端口| 参数值需为端口号  
DistributedOptimizationConfig.spiderConfig.spider_array_group_map_function_threshold| 数组分组算法阈值| 参数值需为正整数，默认为5000000  
DistributedOptimizationConfig.spiderConfig.spider_base_update_thread_proportion| 基础表线程占比| 参数值需为正整数，默认为30  
DistributedOptimizationConfig.spiderConfig.spider_build_index_cores| 构建索引核心数| 参数值需为正整数，默认为4  
DistributedOptimizationConfig.spiderConfig.spider_column_max_load_dictionary_key_size| 数据列最大载入字典数量| 参数值需为正整数，默认为10000  
DistributedOptimizationConfig.spiderConfig.spider_compress_slice_size| 抽数时，每个分片的行数| 参数值需为正整数，默认为100000  
DistributedOptimizationConfig.spiderConfig.spider_core_limit_fraction| spark限制核心任务评分| 参数值需为非负双精度浮点型默认为0.67  
DistributedOptimizationConfig.spiderConfig.spider_create_satellite_async| 异步创建卫星表| 参数值需为布尔型，默认为truetrue：异步创建卫星表false：异步不创建卫星表  
DistributedOptimizationConfig.spiderConfig.spider_deletion_criteria_size_per_execution| 增量删除每次最大计算大小| 参数值需为字符串，默认为128m  
DistributedOptimizationConfig.spiderConfig.spider_double_dictionary_max_key_size| double类型最大字典数量| 参数值需为正整数，默认为10000  
DistributedOptimizationConfig.spiderConfig.spider_engine_use_page| 使用分页引擎| 参数值需为布尔型，默认为truetrue：使用分页引擎false：不使用分页引擎  
DistributedOptimizationConfig.spiderConfig.spider_etl_coalesce_size| etl最大分块数| 参数值需为正整数，默认为10  
DistributedOptimizationConfig.spiderConfig.spider_etl_compute_limit_unit| etl计算单元格限制| 参数值需为正整数，默认为50000000  
DistributedOptimizationConfig.spiderConfig.spider_etl_core_limit| etl限制核心| 参数值需为布尔型，默认为falsetrue：etl限制核心false：etl不限制核心  
DistributedOptimizationConfig.spiderConfig.spider_etl_iterator_repartition_size| etl重分区大小| 参数值需为正整数，默认为20  
DistributedOptimizationConfig.spiderConfig.spider_etl_no_order| etl无序| 参数值需为布尔型，默认为falsetrue：etl无序false：etl有序  
DistributedOptimizationConfig.spiderConfig.spider_etl_output_use_bitmap| ETL生成索引true| 参数值需为布尔型，默认为truetrue：ETL生成索引false：ETL不生成索引  
DistributedOptimizationConfig.spiderConfig.spider_etl_preview_row_count| etl预览行数| 参数值需为字符串，默认为5000  
DistributedOptimizationConfig.spiderConfig.spider_etl_writer_lock_wait| etl写锁等待时间| 参数值需为大于等于-1的整数默认为60000  
DistributedOptimizationConfig.spiderConfig.spider_fast_compute_limit_memory| 快速计算内存限制字节大小| 参数值需为正长整型默认为500000000  
DistributedOptimizationConfig.spiderConfig.spider_fast_compute_limit_row| 快速计算行数限制| 参数值需为正整数，默认为10000000  
DistributedOptimizationConfig.spiderConfig.spider_fast_compute_limit_unit| 快速计算单元格限制| 参数值需为正整数，默认为10000000  
DistributedOptimizationConfig.spiderConfig.spider_fast_etl_cache| 快速计算使用缓存| 参数值需为布尔型，默认为truetrue：快速计算使用缓存false：快速计算不使用缓存  
DistributedOptimizationConfig.spiderConfig.spider_file_max_mmap_size| 文件最大mmap大小| 参数值需为正整数，默认为2147483647  
DistributedOptimizationConfig.spiderConfig.spider_file_mmap_size| 文件mmap大小| 参数值需为正整数，默认为1073741823  
DistributedOptimizationConfig.spiderConfig.spider_first_day_of_week| 星期的第一天| 参数值需为[0, 6]区间内的整数默认值为1  
DistributedOptimizationConfig.spiderConfig.spider_float_dictionary_max_key_size| float类型最大字典数量| 参数值需为正整数，默认为10000  
DistributedOptimizationConfig.spiderConfig.spider_generate_join_cache_in_query| 在查询时生成关联缓存| 参数值需为布尔型，默认为truetrue：在查询时生成关联缓存false：在查询时不生成关联缓存  
DistributedOptimizationConfig.spiderConfig.spider_high_performance_pool_size| 不保证计算性能时，关联和分析表资源池大小| 参数值需为正整数，默认为1000  
DistributedOptimizationConfig.spiderConfig.spider_high_performance_resource_time| 设置更新可占用高性能资源的时间段| 参数值需为字符串，默认为空如需设置晚七点-早八点，请将参数值修改为 19:00:00-8:00:00  
DistributedOptimizationConfig.spiderConfig.spider_ignore_base_update| 是否跳过基础表更新| 参数值需为布尔型，默认为falsetrue：跳过基础表更新false：不跳过基础表更新  
DistributedOptimizationConfig.spiderConfig.spider_index_build_bitmap_dataset| 索引生成使用dataset| 参数值需为布尔型，默认为falsetrue：索引生成使用datasetfalse：索引不生成使用dataset  
DistributedOptimizationConfig.spiderConfig.spider_index_build_bitmap_external| 索引生成使用外排| 参数值需为布尔型，默认为truetrue：索引生成使用外排false：索引不生成使用外排  
DistributedOptimizationConfig.spiderConfig.spider_index_build_bitmap_external_buffer_path| 索引缓存文件路径| 参数值需为字符串默认为distributed/external  
DistributedOptimizationConfig.spiderConfig.spider_index_build_bitmap_external_buffer_size| 索引缓冲大小| 参数值需为正整数，默认为100000  
DistributedOptimizationConfig.spiderConfig.spider_int_dictionary_max_key_size| int类型最大字典数量| 参数值需为正整数，默认为10000  
DistributedOptimizationConfig.spiderConfig.spider_int_distinct_structure| 控制去重记录数的数据结构| 参数值为指定值，默认值为00：表示数据结构为KolobokeIntSet，速度快但内存占用大（平均一个int key占用8字节）1：表示数据结构为RoaringBitmap，速度慢但内存占用小（平均一个int key占用1字节）  
DistributedOptimizationConfig.spiderConfig.spider_join_always_use_sql| 关联始终使用SQL计算| 参数值需为布尔型，默认为falsetrue：关联始终使用SQL计算false：关联始终不使用SQL计算  
DistributedOptimizationConfig.spiderConfig.spider_join_build_index| 关联生成索引| 参数值需为布尔型，默认为truetrue：关联生成索引false：关联不生成索引  
DistributedOptimizationConfig.spiderConfig.spider_join_cache_delete_direct| 关联缓存立刻删除| 参数值需为布尔型，默认为truetrue：关联缓存立刻删除false：关联缓存不立刻删除  
DistributedOptimizationConfig.spiderConfig.spider_join_dot_constant| 关联点常量| 参数值需为字符串，默认为.  
DistributedOptimizationConfig.spiderConfig.spider_join_equal_constant| 关联等号常量| 参数值需为字符串，默认为=  
DistributedOptimizationConfig.spiderConfig.spider_join_huge_table_size| 关联大表大小| 参数值需为非负整数，默认为0  
DistributedOptimizationConfig.spiderConfig.spider_join_left_bracket_constant| 关联左括号常量| 参数值需为字符串，默认为(  
DistributedOptimizationConfig.spiderConfig.spider_join_left_square_bracket_constant| 关联左中括号常量| 参数值需为字符串，默认为[  
DistributedOptimizationConfig.spiderConfig.spider_join_name_simple| 关联使用简单命名| 参数值需为布尔型，默认为falsetrue：关联使用简单命名false：关联不使用简单命名  
DistributedOptimizationConfig.spiderConfig.spider_join_right_bracket_constant| 关联右括号常量| 参数值需为字符串，默认为)  
DistributedOptimizationConfig.spiderConfig.spider_join_right_square_bracket_constant| 关联右中括号常量| 参数值需为字符串，默认为]  
DistributedOptimizationConfig.spiderConfig.spider_join_use_relation| 使用关联缓存| 参数值需为布尔型，默认为truetrue：使用关联缓存false：不使用关联缓存  
DistributedOptimizationConfig.spiderConfig.spider_load_data_buffer_queue_size| 抽数的缓冲队列大小| 参数值需为正整数，默认为100  
DistributedOptimizationConfig.spiderConfig.spider_load_data_buffer_row_size| 抽数的缓冲行大小| 参数值需为正整数，默认为1000  
DistributedOptimizationConfig.spiderConfig.spider_load_use_bitmap| 抽数生成索引| 参数值需为布尔型，默认为truetrue：抽数生成索引false：抽数不生成索引  
DistributedOptimizationConfig.spiderConfig.spider_local_compute_cores| 本地计算核心数| 参数值需为正整数，默认为空  
DistributedOptimizationConfig.spiderConfig.spider_local_default_db| 数据默认DB| 参数值需为字符串，默认为db  
DistributedOptimizationConfig.spiderConfig.spider_local_root_path| 数据抽取存放路径| 参数值需为字符串，默认为../spider  
DistributedOptimizationConfig.spiderConfig.spider_lock_wait_time| 锁的默认等待时间| 参数值需为正整数，默认为1000  
DistributedOptimizationConfig.spiderConfig.spider_long_dictionary_max_key_size| long类型最大字典数量| 参数值需为正整数，默认为10000  
DistributedOptimizationConfig.spiderConfig.spider_low_performance_small_pool_size| 保证计算性能时，关联生成资源池大小| 参数值需为正整数，默认为4  
DistributedOptimizationConfig.spiderConfig.spider_max_rowstream_memory_size| etl rowstream内存限制| 参数值需为正整数，默认为52428800  
DistributedOptimizationConfig.spiderConfig.spider_memory_check_frequency_group| 分组算法内存统计频率| 参数值需为正整数，默认为100000  
DistributedOptimizationConfig.spiderConfig.spider_merge_forbidden_time| 合并禁止时间| 参数值需为字符串，默认为空  
DistributedOptimizationConfig.spiderConfig.spider_number_set_dictionary_max_key_size| 数值类型字典编码是否设置最大字典数量| 参数值需为布尔型，默认为falsetrue：设置最大字典数量false：不设置最大字典数量  
DistributedOptimizationConfig.spiderConfig.spider_page_summary_concurrent_threads| 分页指标计算多线程| 参数值需为布尔型，默认为空true：分页指标计算多线程false：分页指标不计算多线程  
DistributedOptimizationConfig.spiderConfig.spider_partition_limitation| Partition行限制| 参数值需为正整数，默认为1000  
DistributedOptimizationConfig.spiderConfig.spider_partition_merge_policy| partition合并策略| 参数值需为字符串，默认为空  
DistributedOptimizationConfig.spiderConfig.spider_partition_row_size| 分区行数| 参数值需为正整数，默认为10000000  
DistributedOptimizationConfig.spiderConfig.spider_partition_slice_size| 分区抽数时，每个分片的行数| 参数值需为正整数，默认为5000  
DistributedOptimizationConfig.spiderConfig.spider_query_condition_count_restriction| 引擎查询contition数量限制| 参数值需为大于等于-1的整数默认为-1  
DistributedOptimizationConfig.spiderConfig.spider_reduce_row_key_ratio| reduce使用字典的比率| 参数值需为非负双精度浮点型，默认为1.0  
DistributedOptimizationConfig.spiderConfig.spider_relation_column_strategy| 关联列的生成策略| 参数值需为字符串，默认为SectionShrink  
DistributedOptimizationConfig.spiderConfig.spider_relation_matcher_policy| 关联匹配规则| 参数值需为字符串，默认为HeadTail  
DistributedOptimizationConfig.spiderConfig.spider_restrictions_column_long_text| 最长文本限制| 参数值需为正整数，默认为1000  
DistributedOptimizationConfig.spiderConfig.spider_retry_max_times| 重试最大次数| 参数值需为正整数，默认为2  
**DistributedOptimizationConfig.spiderConfig.spider_row_index_strategy**|  分析表行索引优化| 参数值需为布尔型，默认为falsetrue：分析表行索引优化false：分析表行索引不优化  
DistributedOptimizationConfig.spiderConfig.spider_satellite_creation_step| 卫星表创建步长| 参数值需为正整数，默认为10000000  
DistributedOptimizationConfig.spiderConfig.spider_section_merge_large_section_count| section合并大块数量| 参数值需为正整数，默认为6  
DistributedOptimizationConfig.spiderConfig.spider_section_merge_policy| section合并策略| 参数值需为字符串，默认为grouping  
DistributedOptimizationConfig.spiderConfig.spider_section_merge_row_threshold_factor| section合并行数阈值| 参数值需为正整数，默认为1000000  
DistributedOptimizationConfig.spiderConfig.spider_section_merge_small_section_count| section合并小块数量| 参数值需为正整数，默认为4  
DistributedOptimizationConfig.spiderConfig.spider_spark_driver_use_random_port| spark driver使用随机端口| 参数值需为布尔型，默认为falsetrue：spark driver使用随机端口false：spark driver不使用随机端口  
DistributedOptimizationConfig.spiderConfig.spider_spark_local_threads| spark本地线程数| 参数值需为正整数，默认为空  
DistributedOptimizationConfig.spiderConfig.spider_sql_merge_table| 使用sql合并表| 参数值需为布尔型，默认为truetrue：使用sql合并表false：不使用sql合并表  
DistributedOptimizationConfig.spiderConfig.spider_stream_partition_estimated_byte| 流式分区预估大小| 参数值需为正整数，默认为2000000000  
DistributedOptimizationConfig.spiderConfig.spider_submit_spark_thread_count| 提交spark线程数| 参数值需为正整数，默认为5  
DistributedOptimizationConfig.spiderConfig.spider_table_estimate_strategy| 估算表大小的方式| 参数值需为字符串，默认为SAMPLE  
DistributedOptimizationConfig.spiderConfig.spider_temp_folder_path_for_spark| spark临时文件路径| 参数值需为字符串默认为/root/temp/spark  
DistributedOptimizationConfig.spiderConfig.spider_update_fast_compute_limit_cell| 分析用户自助数据集磁盘占用大小快速分析生成过程中支持的最大单元格数量| 参数值需为正整数，默认为100000000  
DistributedOptimizationConfig.spiderConfig.spider_updated_background| 增量更新合并是否后台执行| 参数值需为布尔型，默认为falsetrue：增量更新合并后台执行false：增量更新合并不在后台执行  
DistributedOptimizationConfig.spiderConfig.spider_updated_partition_num| 触发合并的更新分区数| 参数值需为正整数，默认为2  
DistributedOptimizationConfig.spiderConfig.spider_use_pin_yin_sort| 使用中文拼音排序| 参数值需为布尔型，默认为falsetrue：使用中文拼音排序false：不使用中文拼音排序  
ESDEngineConfig.dataModelMaxSize| 允许缓存的数据集最大数据量| 参数值需为正整数，默认为500000  
ESDEngineConfig.maxCacheEntries| 最大缓存数量| 参数值需为正整数，默认为10000  
ESDEngineConfig.maxIdleTime| 终止前最大空闲时间| 参数值需为正整数，默认为259200000  
ESDEngineConfig.maxPredictCacheEntries| 参数预测最大缓存数量| 参数值需为正整数，默认为5000  
ESDEngineConfig.maxSingleTemplateCacheEntries| 单模板最大缓存数量| 参数值需为正整数，默认为1000  
ESDEngineConfig.schedulePoolSize| 调度器线程池大小| 参数值需为正整数，默认为15  
EmailServerConfig.debugEnable| 邮件发送时，是否开启debug日志| 参数值需为布尔型，默认为falsefalse：邮件发送时，不开启debug日志true：邮件发送时，开启debug日志  
EmailServerConfig.smtpConnectionTimeout| 连接时间限制，单位毫秒。用于限制跟邮件服务器建立连接消耗的时间长短| 参数值需为正整数，默认为60000  
FSConfig.authorizeAttr.postAuthority| 按职位分配权限的开关| 参数值需为布尔型，默认为falsefalse：关闭按职位分配权限true：开启按职位分配权限  
FSConfig.loginConfig.fWords| LDAP认证用户名登录搜索字段。值格式为：["值1","值2"]| 参数值格式为：["值1","值2"]参数值不允许为空，参数长度不允许为0参数默认值为["sAMAccountName","cn","userPrincipalName","uid","displayName","name","sn"]  
FSConfig.loginConfig.forceRedirectAfterLogin| 登录后强制跳转至： http://ip:port/webroot/decision/| 参数值需为布尔型，默认为falsefalse：登录后不强制跳转true：登录后强制跳转  
FSConfig.loginConfig.ldapTimeout| ldap认证登录超时设置，默认为-1不设置超时，单位为毫秒| 参数值需为正整数默认值-1表示不设置超时  
FSConfig.passports.2.ldapMaxPoolSize| ldap认证并发数限制，默认为0不限制|   
  
FeiShuConfig.checkRedirectDomainEnable| 开启或关闭飞书插件单点登录域名一致性校验| 参数值为布尔型，默认为truetrue：开启飞书插件单点登录域名一致性校验false：关闭飞书插件单点登录域名一致性校验  
FileServerMonitorConfig.messageInterval| ftp 异常消息通知频率，单位h| 参数值需为正长整型默认值为1  
FineClusterConfig.params.encrypt| 集群通信加密开关，默认为false| 参数值需为布尔型，默认为falsefalse：集群通信不加密true：集群通信加密  
FineClusterConfig.params.ipStackType| 集群通信方式| 参数值默认为ipv4， 可配置ipv6  
FineClusterConfig.startPorts.core| 集群通讯核心通道| 参数值需为端口值，默认值为7800  
FineClusterConfig.startPorts.db_cache| 集群通讯数据库缓存通道| 参数值需为端口值，默认值为7850  
FineClusterConfig.startPorts.file_sync| 集群通讯文件同步通道| 参数值需为端口值，默认值为7830  
FineClusterConfig.startPorts.general_cache| 集群通讯通用缓存通道| 参数值需为端口值，默认值为7840  
FineClusterConfig.startPorts.member| 集群通讯成员管理通道| 参数值需为端口值，默认值为7870  
GcConfig.gcThreshold| 模板版本控制存储优化条件阀值，单位为文件个数| 参数值需为非负整型默认值为300  
GeneralDataConfig.showTableDataExceptionMsg| 是否展示数据集报错信息| 参数值需为布尔型，默认为truefalse：不展示数据集报错信息true：展示数据集报错信息  
Html5Config.isJoinProductPlan| HTML5 允许关闭开发者计划，用户可以手动关闭是否加入产品改良计划，进一步的保护用户的隐私安全| 参数值需为布尔型，默认为truefalse：关闭开发者计划true：开启开发者计划  
IntelliReleaseConfig.defaultCellCount| 待杀会话格子数的默认基数| 参数值需为长整型默认值为1000000  
IntelliReleaseConfig.highInterruptAgainRate| 高负载时第二次释放超过（默认值格子数*此比例）的会话| 参数值需为非负双精度浮点型默认值为0.6  
IntelliReleaseConfig.highInterruptRate| 高负载时第一次释放超过（默认值格子数*此比例）的会话| 参数值需为非负双精度浮点型默认值为0.8  
IntelliReleaseConfig.highKillRate| 高负载第一次释放的会话比例超过此值不触发第二次| 参数值需为非负双精度浮点型默认值为0.1  
IntelliReleaseConfig.interruptRate| 待杀会话格子数的默认比例| 参数值需为非负双精度浮点型默认值为0.3  
IntelliReleaseConfig.jvmSupport| 当前版本jdk是否支持智能释放| 参数值需为布尔型，默认为truefalse：当前版本jdk不支持智能释放true：当前版本jdk支持智能释放  
IntelliReleaseConfig.releaseSessionInteval| 释放触发的时间间隔| 参数值需为正整型默认值为20  
IntelliReleaseConfig.terribleInterruptAgainRate| 超高负载时第二次释放超过（默认值格子数*此比例）的会话| 参数值需为非负双精度浮点型默认为0.4  
  
IntelliReleaseConfig.terribleInterruptRate| 超高负载时第一次释放超过（默认值格子数*此比例）的会话| 参数值需为非负双精度浮点型默认为0.6  
IntelliReleaseConfig.terribleKillRate| 超高负载第一次释放的会话比例超过此值不触发第二次| 参数值需为非负双精度浮点型默认为0.2  
IntelliReleaseConfig.waitInLineRate| 每个会话在高负载有此几率排队| 参数值需为双精度浮点型默认为0.9  
JarConsistenceConfig.messageInterval| jar不一致异常消息通知频率，单位h| 参数值需为正长整型默认值为6  
LanguageConfig.locale| 平台全局的语言设置| 默认值为zh_CNzh_CN：简体中文zh_TW：繁体中文en_US：英文ja_JP：日文ko_KR：韩文  
LoadConfig.majorExtremeTerribleThreshold| majorgc后，残留在老年代对象大小与老年代大小的比值超过这个值算是极限负载| 参数值需为非负双精度浮点型默认为0.95  
LoadConfig.majorHighThreshold| majorgc后，残留在老年代对象大小与老年代大小的比值超过这个值算是高负载| 参数值需为非负双精度浮点型默认为0.7  
LoadConfig.majorTerribleThreshold| majorgc后，残留在老年代对象大小与老年代大小的比值超过这个值算是超高负载| 参数值需为非负双精度浮点型默认为0.85  
LoadConfig.minorHighThreshold| minorgc后，晋升到老年代的对象速率与eden区的比值大小超过这个值算是高负载| 参数值需为非负双精度浮点型默认为0.04  
LoadConfig.minorMidThreshold| minorgc后，晋升到老年代的对象速率与eden区的比值大小超过这个值算是中等负载| 参数值需为非负双精度浮点型默认为0.02  
LoadConfig.minorTerribleThreshold| minorgc后，晋升到老年代的对象速率与eden区的比值大小超过这个值算是超高负载| 参数值需为非负双精度浮点型默认为0.06  
MarketConfig.cloudOperationMaintenanceId| 重置云端运维应用ID| 参数值默认为您的云端运维应用ID  
MobileConfig.appMsgProxy| App 消息代理注：仅对移动端生效| 参数值为非空字符串默认值为__EMPTY__代理服务器地址格式为：http://ip:port/mobile/push/message/send  
MobileConfig.disableEncryptPassword| 控制移动端登录的密码是否加密注：仅对移动端生效| 参数值需为布尔型，默认为falsefalse：移动端登录的密码不加密true：移动端登录的密码加密  
MobileConfig.emptyDirVisible| 控制在移动端（APP、HTML5）是否显示空目录注：仅对移动端生效。| 参数值需为布尔型，默认为falsetrue：显示空目录false：不显示空目录  
MobileConfig.landscapeLayoutType| 控制移动端重布局横屏状态下的布局类型注：仅对移动端生效| 参数值可设置： 0 、1 。默认值为 0 0 ：横屏展示时，一页展示一个组件，通过按钮，左右切换组件1 ：横屏展示时，流式布局。横向充满组件，纵向向下滑动查看模板。与竖屏查看方式一致  
MobileConfig.modulesConfigAvailable| 开启或关闭移动平台模块配置功能注：仅对移动端生效| 参数值需为布尔型，默认为falsefalse：关闭移动平台模块配置功能true： 开启移动平台模块配置功能  
MobileConfig.persistedAttach| 是否在启动服务器的时候持久化定时调度图片注：仅对移动端生效| 参数值需为布尔型默认第一次启动为false，后为truefalse：在启动服务器的时候持久化定时调度图片true：在启动服务器的时候不持久化定时调度图片  
MobileConfig.productPlan| 是否加入开发者计划注：仅对移动端生效| 参数值需为布尔型，默认为truefalse：不加入开发者计划true：加入开发者计划  
MobileConfig.requiredDisplayDeviceType| 设置移动端设备展示类型注：仅对移动端生效| 参数值如下，默认值为 defaultdefault：手机展示手机，pad 展示 pad  
phone：手机 & pad 都展示手机效果  
  
MobileConfig.templateFetchTimeout| 模板超时时间注：仅对移动端生效| 参数值需为整型，默认值为 -1字段值小于等于 0 时，填报请求、表单数据、请求组件数据限制超时时间为30s字段值大于 0 时，按照设置的时间生效，单位秒请求（填报请求、表单数据、请求组件数据）没有返回结果则取消加载；其中填报请求、表单数据超时会弹出提示「模板请求超时，请联系管理员增加请求超时时间」  
ParseCheckConfig.allowDrawing| 当html解析报错时（各个导出场景遇到不支持的标签和属性），是否允许将html画成图| 参数值需为布尔型，默认为truefalse：当html解析报错时，不允许将html画成图true：当html解析报错时，允许将html画成图  
QuartzConfig.maxConnections| FR定时调度模块最大连接数| 参数值需为正整型默认值为50  
QuartzConfig.threadCount| FR定时调度模块最大线程数| 参数值需为正整型默认值为100  
RedisClusterConfig.maxConnection| Redis Cluster 连接池最大实例总数| 参数值需为正整型默认值为200  
RedisClusterMonitorConfig.messageInterval| Redis节点异常消息通知频率，单位h| 参数值需为正长整型默认值为6  
RedisConfig.database| Redis 指定数据库| 参数值需为整型默认值为0  
RedisConfig.expireStateRemoveInterval| 状态服务器过期 key 删除间隔时间，单位ms| 参数值需为正整型默认值为300000  
RedisConfig.maxConnection| Redis连接池最大实例总数| 参数值需为正整型默认值为200  
RemoteDesignConfig.avoidTempAuthValid| 远程设计支持数字签名预览| 参数值需为布尔型，默认为truefalse：远程设计不支持数字签名预览true：远程设计支持数字签名预览  
Reuse.exportEnable| 复用导出时，是否展示导出按钮| 参数值需为布尔型，默认为falsefalse：不展示导出按钮true：展示导出按钮  
ScheduleSettingConfig.taskTimeout| 定时任务超过时间，默认5分钟| 参数值需为正长整型默认值为300000  
ScheduleSettingConfig.timeoutRemind| 定时调度任务是否开启监控日志超时提醒| 参数值需为布尔型，默认为falsefalse：定时调度任务不开启监控日志超时提醒true：定时调度任务开启监控日志超时提醒  
SecurityConfig.AllowDeleteLog| 是否允许前端删除日志| 参数值为布尔型，默认为 truefalse：「智能运维>平台日志>全局设置」不可见手动清理日志功能true：「智能运维>平台日志>全局设置」可见手动清理日志功能  
SecurityConfig.forbidLoginNoEncryption| 是否允许接口中传输明文密码| 参数值为布尔型，默认为 falsefalse：支持明文和加密两种方式true：只支持密文  
SecurityConfig.frontSeed| 用于给前端加密提供秘钥| 参数值为16位大小写字母初始是随机的16位大小写字母字符串，可自行修改  
SecurityConfig.hideFrontSeed| 返回给前端的接口数据中是否隐藏 FrontSeed| 参数值为布尔型，默认为 falsefalse：不隐藏true：隐藏  
SentinelConfig.abnormalDataTextMaxLength| 数据预警异常数据字符限制：控制预警推送中变量的内容长度| 参数值需为正整型，默认值为 5000  
  
SentinelConfig.sentinelResultSetLimit| 数据预警结果集行数限制，符合预警条件的数据量达到该参数值即停止计算| **仅对V1.6.9及以上版本的数据预警插件生效** 参数值为正整数，不建议调大该参数，否则可能由于结果集过大导致工程宕机默认值为1000000  
SentinelConfig.showDetailAbnormalData| 控制数据预警推送的异常数据条数| ****仅对V1.6.9及以上版本的数据预警插件生效**** 参数值需为布尔型，默认为truetrue：“异常数据”变量中的内容包含全部异常数据false：“异常数据”变量中的内容包含对应条件下的异常数据  
ServerConfig.cookiePath| cookie路径| 参数值需为非空字符串初始值为/注：请在部署工程时配置，尤其是多个工程部署在同一服务器下，且使用了相同域名时，请务必配置。否则会造成浏览器存储多个cookie，需要每个用户手动清除cookie才能登录成功  
ServerConfig.tokenFromCookie| 开启后后台校验token时可从cookie中取，解决httponly下后台单点和跨域单点登录失败的问题| 参数值需为布尔型，默认为falsefalse：后台校验token时不可从cookie中取true：后台校验token时可从cookie中取  
ServerPreferenceConfig.errorTemplate| FR模板报错页面，可参考帆软官方帮助文档，自定义模板报错页面| 参数值为自定义报错页面链接默认为__EMPTY__  
ServerPreferenceConfig.useOptimizedUPM| 配置是否开启新插件管理| 参数值需为布尔型，默认为falsefalse：不开启新插件管理true：开启新插件管理  
SmartTemplateCacheConfig.enable| 是否开启智能模板缓存| 参数值需为布尔型，默认为truefalse：不开启智能模板缓存true：开启智能模板缓存  
SmartTemplateCacheConfig.maxElementSizeMB| 缓存容量限制，单位MB| 参数值需为整数，单位MB默认值为0  
SystemConfig.hideVersion| 是否隐藏system info中的版本信息| 参数值需为布尔型，默认为falsefalse：不隐藏system info中的版本信息true：隐藏system info中的版本信息  
SystemOptimizationConfig.ClientMasterId| Web 集群有数据的节点| 参数值需为字符串是 Web 集群，指定的数据请求，更新，有数据的那台机器的 Id  
SystemOptimizationConfig.baseTableLoadDynamicThreadCoreSizeStr| 基础表更新线程限制| 需要先设置DistributedOptimizationConfig.spiderConfig.spider_high_performance_resource_time，方可配置该参数参数值：默认为__EMPTY__，格式如下调度高性能线程数:调度低性能线程数,引擎高性能线程数:引擎低性能线程数  
SystemOptimizationConfig.biClusterMasterNodeHostName| BI 集群的主节点的 hostname| 参数值需为字符串初始值为__EMPTY__  
SystemOptimizationConfig.bigDataModeThreshold| BI进入大数据模式的阈值，分组数大于此值进入大数据模式| 参数值需为正整型默认值5000  
SystemOptimizationConfig.cacheDiskPath| 直连缓存写磁盘绝对路径| 参数值需为字符串初始值为__EMPTY__  
SystemOptimizationConfig.cacheDiskPercent| 直连缓存写磁盘的最大空间默认占BI磁盘目录的比例，默认20%即0.2| 参数值需为0~1之间的小数，默认值为0.2  
SystemOptimizationConfig.cacheHeap| 缓存个数：除去关联维表缓存和分页缓存的其他缓存| 参数值需为非负整型默认不配置时，大数据集缓存100个，小数据集缓存10000个设置成0，表示缓存个数无限制，修改后需要重启生效  
SystemOptimizationConfig.cacheIdleSeconds| 缓存过期时间| 参数值需为正长整型默认值为300  
SystemOptimizationConfig.cacheLargeMemPercent| 大缓存池内存占比| 参数值需为非负双精度浮点型默认为0.2  
SystemOptimizationConfig.cacheMiddleMemPercent| 中缓存池内存占比| 参数值需为非负双精度浮点型默认为0.05  
SystemOptimizationConfig.cacheSmallMemPercent| 小缓存池内存占比| 参数值需为非负双精度浮点型默认为0.01  
SystemOptimizationConfig.cacheStrategy| 缓存策略| 参数值需为字符串默认为mem  
SystemOptimizationConfig.chartBigDataNum| 限制大数据图表的数量| 参数值需为整型默认值为3  
SystemOptimizationConfig.chartDataThreadPoolNum| 图表线程池数量| 参数值需为非负整型，默认值为80代表关闭线程池，关闭后，BI的线程栈将不会出现chart-group-data-pool开头的线程直连时该参数无意义  
SystemOptimizationConfig.clearEntityStrategy| 获取FineBI更新任务记录的清理策略清理策略| 参数默认值为__EMPTY__，仅保留一个月的更新任务记录参数格式为：{策略序号}:{清理几月数据},{清理时间（时）},{清理时间（分）},{清理周期（秒）};例如：  
策略1，清理3月前数据，每2天执行一次，4点20分执行  
策略2，清理1月前的数据，每30天执行一次，2点50执行。  
则该参数为：1:3,4,20,172800;2:1,2,50,2592000  
SystemOptimizationConfig.compressThreadCount| 数据源数据压缩指定线程数| 参数值默认为-1  
SystemOptimizationConfig.confLockTimeOutTime| 配置锁超时时间设置，单位为秒  
| 参数值需为正长整型默认值为30  
SystemOptimizationConfig.dashboardEditLimit| 仪表板编辑时的行数限制（不选中全部数据）| 参数值需为整型默认值为10000  
SystemOptimizationConfig.detailUseColumnarCompress| 明细表是否启用列压缩| 参数值需为布尔型，默认为truefalse：明细表不启用列压缩true：明细表启用列压缩  
SystemOptimizationConfig.directCacheExpiredCheckPeriod| 定时任务清理失效缓存对象的执行周期| 参数值需为整型，单位秒默认值为60  
SystemOptimizationConfig.directMemoryEngineLimitRows| 直连新的内存引擎缓存数据的行数限制| 参数值需为整型默认值为100000  
SystemOptimizationConfig.directUseAllData| 直连全部数据是否可用，默认不可用| 参数值需为布尔型，默认为truefalse：直连全部数据可用true：直连全部数据不可用  
SystemOptimizationConfig.etlEditSourceRowLimit| 编辑支持的最大数据量行数限制| 参数值需为正整数默认为10000000  
SystemOptimizationConfig.excelExtractDataBase| Excel数据抽取  
直连的关联可选表存在限制，如果系统参数为 Excel 数据抽取的话，Excel 表才可以配置关联| 参数值需为布尔型，默认为falsefalse：直连的 Excel 表不可以配置关联true：直连的 Excel 表可以配置关联  
SystemOptimizationConfig.excelExtractMaxLimitRows| 直连excel生成临时表时的行数限制| 参数值需为整型默认值为10000  
SystemOptimizationConfig.extractionSettingSenseSwitch| 抽取设置感知开关| 参数值需为布尔型，默认为falsefalse：不显示抽取设置感知开关true：显示抽取设置感知开关  
SystemOptimizationConfig.fastTableLoadDynamicThreadCoreSizeStr| 快速分析更新线程限制| 需要先设置DistributedOptimizationConfig.spiderConfig.spider_high_performance_resource_time，方可配置该参数参数值：默认为__EMPTY__，格式如下调度高性能线程数:调度低性能线程数,引擎高性能线程数:引擎低性能线程数  
SystemOptimizationConfig.fieldInfoTimeoutSeconds| 从数据源取字段信息的超时时间| 参数值需为长整型默认值为-1  
SystemOptimizationConfig.firstDayofWeek| 每周的第一天是星期几| 参数值需为整型默认值为0  
SystemOptimizationConfig.fullDataSearchThreadLimit| 控制全局最大搜索并发数| 参数值需为长整型默认值为-1-1：表示不设限制  
SystemOptimizationConfig.groupUseColumnarCompress| 分组表是否启用列压缩| 参数值需为布尔型，默认为truefalse：分组表不启用列压缩true：分组表启用列压缩  
SystemOptimizationConfig.ignoreBaseTableRedMarkCheck| 基础表忽略标红| 参数值需为布尔型，默认为truefalse：分组表不启用列压缩true：分组表启用列压缩  
SystemOptimizationConfig.inheritPermissionAndRelation| 设置主题内原始表权限继承按钮的默认开关状态| 参数值需为布尔型，默认为truefalse：默认关闭true：默认开启  
SystemOptimizationConfig.maxCutlnLineCount| 插队的更新任务数量| 参数值需为正整数，默认为5  
SystemOptimizationConfig.maxUpdateTimeoutCancelTime| 智能查杀最大超时中止时间，单位秒，默认值：12*3600| 参数值需为正整数，默认为43200  
SystemOptimizationConfig.memoryWarningSize| sql数据集数据量告警值| 参数值需为整型默认值为100000000  
SystemOptimizationConfig.needTreatRedMark| 是否修复标红的自助数据集| 参数值需为布尔型，默认为falsefalse：不修复标红的自助数据集true：修复标红的自助数据集  
SystemOptimizationConfig.openUpdateIntelligentKill| 是否开启更新智能查杀| 参数值需为布尔型，默认为truefalse：不开启更新智能查杀true：开启更新智能查杀  
SystemOptimizationConfig.optimizeSqlAlias| 是否优化SQL别名（开启会把SQL中的别名全部重设一遍）| 参数值需为布尔型，默认为truefalse：不优化SQL别名true：优化SQL别名  
SystemOptimizationConfig.queryConditionCountRestriction| 明细过滤条件个数限制| 参数值需为整型默认值为1000  
SystemOptimizationConfig.quickTaskMaxTimeoutThreshold| 快任务（一般指耗时短的任务）的最大超时阈值，单位秒，默认值3600，小于该阈值的任务，超时时间为阈值*2| 参数值需为正整型默认值3600  
SystemOptimizationConfig.readRelationFromDbSource| 添加db表时，是否要读取数据库中的关联| 参数值需为布尔型，默认为truefalse：添加db表时不读取数据库中的关联true：添加db表时读取数据库中的关联  
SystemOptimizationConfig.reportShareType| 模板分享是否使用创建者权限| 参数值为整型默认值为0  
SystemOptimizationConfig.resultSetRowLimit| 数据访问量限制参数，默认100w| 参数值需为正整型默认值1000000  
SystemOptimizationConfig.scaleLowerLimit | 限制仪表板预览缩放下限| 参数值为数值类型float默认值为-1.0，请勿擅自修改  
SystemOptimizationConfig.scaleUpperLimit| 限制仪表板预览缩放上限| 参数值为数值类型float默认值为-1.0，请勿擅自修改  
SystemOptimizationConfig.scheduleTaskThreadsLimit| BI定时调度任务最大并发线程数| **BI功能独有** 参数值需为正整数默认值为3  
SystemOptimizationConfig.schedulerMergeTimeSeconds| 多少秒进行一次定时任务的合并| 参数值需为整型默认值为5  
SystemOptimizationConfig.shieldFunction| 限制是否使用主题内外的表| **BI功能独有** 参数值需为布尔型，默认为truetrue ：限制使用主题内的表false ：不限制使用主题内外的表  
SystemOptimizationConfig.slowTaskMaxTimeoutThreshold| 慢任务（一般指耗时长的任务）的最大超时阈值，单位秒，默认值8*3600，对应的是这个超时计算公式中的8h| 参数值需为整型默认值为2880  
SystemOptimizationConfig.subjectDraftSavePeriod| 主题草稿保存间隔，单位为分钟，小于等于零代表不保存| **BI功能独有******参数值需为正整数， 单位为分钟小于等于零代表不保存默认值为2  
SystemOptimizationConfig.subjectVersionLimit| 主题版本数量限制，大于等于零| **BI功能独有** 参数值需为正整数默认值为5  
SystemOptimizationConfig.tableLoadDataLimit| 限制数据库取数的数量| 参数值需为正整型默认值为50000  
SystemOptimizationConfig.tableLoadThreadPoolNum| 更新线程数量| 参数值需为整型默认值为20  
SystemOptimizationConfig.threadPoolStrategy| 更新线程池策略  
| 参数值如下，默认为dynamicdynamic：根据内存来算，1G=1个线程  
static：固定线程数量，和TableloadThreadPoolNum一起使用  
SystemOptimizationConfig.timeoutCancelRetryInterval| 智能查杀误差杀重试间隔，单位秒，默认值3600| 参数值需为正整型默认值为3600  
SystemOptimizationConfig.useAllVisibleDataForSentinel| BI 数据预警是否使用全部预览可见数据| 参数值需为布尔型，默认为truefalse：保留仪表板默认过滤情况，用户仅可使用仪表板默认展示数据进行预警，预览时调整的过滤条件不生效true：应用全量仪表板数据（用户可见即可用）  
SystemOptimizationConfig.useColumnarCompress| 分组表是否启用列压缩| 参数值需为布尔型，默认为truefalse：分组表不启用列压缩true：分组表启用列压缩  
SystemOptimizationConfig.usePagingCache| 是否开启分页缓存| 参数值需为布尔型，默认为truefalse：不开启分页缓存true：开启分页缓存  
SystemOptimizationConfig.excelExportThreadTimeoutLimit| 仪表板导出 excel 超时打断导出时长超出设置时间则打断| 参数值需为整型单位为分钟默认值为 -1，代表不限制时间  
TemplateAuthConfig.digitalAuthAvailable| 模板认证-数字签名功能是否可使用| 参数值如下，默认为truefalse：管理员无法使用模板认证-数字签名功能true：管理员可使用模板认证-数字签名功能  
TemplateIOErrorContextConfig.showTemplateMissingPlugin| 打开模板是否提示缺少插件| 参数值需为布尔型，默认为falsefalse：不提示缺少插件true：提示缺少插件  
UpdateConfig.launchSwitchMap.plugins| 插件自动更新的启动更新是否开启| 如需关闭工程启动后的插件自动更新，请将参数值修改为false，否则无需改动  
WeLinkConfig.checkRedirectDomainEnable| 开启或关闭WeLink插件单点登录域名一致性校验| 参数值为布尔型，默认为truetrue：开启WeLink插件单点登录域名一致性校验false：关闭WeLink插件单点登录域名一致性校验  
WebSecurityConfig.cacheControlExpiresHeader| 浏览器缓存禁用header expires的值| 参数值如下，默认值为00：代表着过去的日期，即该资源已经过期<http-date>：在指定日期后，响应过期  
WebSecurityConfig.cacheControlHeader| 浏览器缓存禁用header cache-control的值| 参数值如下，默认值为no-cacheno-cache：在发布缓存副本之前，强制要求缓存把请求提交给原始服务器进行验证(协商缓存验证)max-age=<seconds>：设置缓存存储的最大周期，超过这个时间缓存被认为过期(单位秒)  
WebSecurityConfig.cacheControlPragmaHeader| 浏览器缓存禁用header pragma的值| 参数值为no-cache  
WebSecurityConfig.contentSecurityPolicyHeader| csp内容安全策略header content-security-policy的值| 参数值如下，默认值为object-src 'self'1）object-src 'self'：限制<object>、<embed>、<applet>标签的源地址且仅允许与当前来源（而不是其子域）匹配2）object-src uri限制<object>、<embed>、<applet>标签的源地址  
且上述标签中地址仅指定URL允许加载3）default-src https:禁用不安全的内联/动态执行, 只允许通过 https加载这些资源 (images, fonts, scripts, etc.)  
WebSecurityConfig.contentTypeOptionsHeader| 内容嗅探攻击防护header x-content-type-options的值| 参数值为nosniff  
WebSecurityConfig.enableParameterVerify| 安全参数校验enableParameterVerify的值| 参数值为布尔型，默认为truetrue：校验enableParameterVerify的值false：不校验enableParameterVerify的值  
WebSecurityConfig.fileInspectorType| 开启了安全管理的文件校验后，用此配置文件上传校验类型| 参数值如下，默认为10：综合，后缀不在白名单内放行，否则校验头1：白名单，后缀在白名单且头匹配的才放行2：黑名单，后缀不在黑名单内放行  
WebSecurityConfig.frameOptionsHeader| 点击劫持攻击防护header x-frame-options的值| 参数值如下，默认值为SAMEORIGINDENY：浏览器会拒绝当前页面加载任何frame页面  
SAMEORIGIN：frame页面的地址只能为同源域名下的页面  
ALLOW-FROM origin：允许frame加载的页面地址  
WebSecurityConfig.hstsHeader| hsts header strict-transport-security的值| 参数值为如下，默认值为max-age=31536000; includeSubDomains1）max-age=<expire-time>：设置在浏览器收到这个请求后的XXX秒的时间内凡是访问这个域名下的请求都使用HTTPS请求2）max-age=<expire-time>; includeSubDomains：设置在浏览器收到这个请求后的XXX秒的时间内凡是访问这个域名下的请求都使用HTTPS请求。此规则也适用于该网站的所有子域名3）max-age=<expire-time>; preload：设置在浏览器收到这个请求后的XXX秒的时间内凡是访问这个域名下的请求都使用HTTPS请求。预加载HSTS  
WebSecurityConfig.loginValidateStrict| 用于限制跨域登录接口，以及cas后台登录接口的使用，如果配置true，则不能使用这俩接口| 参数值需为布尔型，默认为falsefalse：不限制跨域登录接口和cas后台登录接口的使用true：限制跨域登录接口和cas后台登录接口的使用  
WebSecurityConfig.verifyTokenSync| Token一致性检测| 参数值需为布尔型，默认为falsetrue：不校验token一致性false：校验token一致性  
WebSecurityConfig.xssProtectionHeader| xss攻击防护header x-xss-protection的值| 参数值如下，默认值为1; mode=block0：禁止XSS过滤1：启用XSS过滤，如果检测到跨站脚本攻击，浏览器将清除页面，删除不安全的部分1; mode=block：启用XSS过滤，如果检测到攻击，浏览器将不会清除页面，而是阻止页面加载1; report=<reporting-uri>：启用XSS过滤如果检测到跨站脚本攻击，浏览器将清除页面，并使用CSP reporting-uri的功能发送违规报告  
WebSocketConfig.hostName| Websocket 监听 IP 设置| 参数值为服务器内置网卡或对外 IP默认为0.0.0.0  
WebSocketConfig.port| websocket服务器监听端口| 参数值为端口数组["port1","port2"]port必须属于(1024,65535]BI默认值为48888FR默认值为["38888","39888"]  
WebSocketConfig.randomSession| 控制不同tab页下websocket连接的会话id是否相同| 参数值为布尔型，默认为falsetrue：生成不同会话idfalse：保持同一会话id  
WebSocketConfig.requestPorts| websocket前端请求端口| 参数值为端口数组["port1","port2"]port必须属于(1024,65535]BI默认值为["48889"]FR默认值为["38889"]  
WebSocketConfig.trustStore| 信任证书的文件存放路径| 参数值为非空字符串，尽量使用绝对路径默认值为__EMPTY__  
WebSocketConfig.trustStoreFormat| 信任证书的类型| 参数值为JKS或PKCS12如果是pfx证书，改成PKCS12默认值为JKS  
WebSocketConfig.trustStorePassword| 信任证书使用时的申请秘钥| 参数值为非空字符串，尽量使用绝对路径默认值为__EMPTY__  
WebSocketConfig.webSocketTokenInHeader| socket 通信 token 传递方式| 参数值需为布尔型，默认为falsetrue：token 从请求头传输false：token 从 url 传输  
WeiXinConfig.checkRedirectDomainEnable| 开启或关闭微信插件单点登录域名一致性校验| 参数值为布尔型，默认为truetrue：开启微信插件单点登录域名一致性校验false：关闭微信插件单点登录域名一致性校验  
WorkflowAuthorityConfig.compatible| 多级上报的独立链接，首次登录时，页面会跳出弹窗提示：目录权限中有关于上报页面的权限配置，是否从目录权限中同步权限配置该参数用于控制之后是否弹出提示| 参数值需为布尔型，默认为falsetrue：不弹出false：弹出  
WriteOptimizationConfig.asyncInsert| 填报插入删除行局部刷新是否开启| 参数值需为布尔型，默认为falsetrue：填报插入删除行局部刷新不开启false：填报插入删除行局部刷新开启  
WriteOptimizationConfig.transactionRepeatableRead| 填报提交是否使用可重复读事务隔离级别| 参数值为布尔型，默认为truetrue：填报提交使用可重复读事务隔离级别false：填报提交不使用可重复读事务隔离级别  
WriteOptimizationConfig.verifyCustomValue| 填报单元格控件自定义值校验是否开启| 参数值为布尔型，默认为truetrue：填报单元格控件自定义值校验开启false：填报单元格控件自定义值校验关闭  
ManagementExportConfig.streamMode| 权限导出是否使用流模式预览| 参数值需为布尔型，默认为falsetrue：权限导出插件内置的数据集无法在设计器预览false：权限导出插件内置的数据集可以在设计器预览  
### 2.4 重启服务器
按照参数规则修改配置后，点击「保存」，跳出提示框：您修改的参数在重启后生效，请重启服务器。
重启 BI 服务器后，配置生效。
![image.png](https://help.fanruan.com/core/style/lod.png)
注：若不按照 2.3 节的参数规则配置，参数值校验失败，将跳出提示框：配置项值校验不通过，保存失败。
![image.png](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：配置库表结构](<index.php?doc-view-819.html>)
[下一篇：填报修改fine_conf_entity ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2157.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
