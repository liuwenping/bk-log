# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-LOG 蓝鲸日志平台 available.
Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
License for BK-LOG 蓝鲸日志平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class CreateSampleSetCls(object):
    """创建样本集"""

    scene_name: str
    sample_type: str
    project_id: int
    sample_set_name: str
    description: str
    processing_cluster_id: int
    storage_cluster_id: int
    ts_freq: int = 0
    sensitivity: str = "private"
    modeling_type: str = "aiops"


@dataclass
class FieldsCls(object):
    field_name: str
    field_type: str
    field_alias: str
    generate_type: str
    rt_field_name: str
    require_type: str
    attr_type: str
    field_index: int
    description: str
    properties: Dict = field(default_factory=dict)


@dataclass
class AddResultTableToSampleSetCls(object):
    """
    把rt添加到stag表
    """

    sample_set_id: int
    result_table_id: str
    fields: List[FieldsCls]
    group_curve: bool = False
    group_fields: List[str] = field(default_factory=list)
    select_all_lines: bool = False
    lines: List[str] = field(default_factory=list)
    aggregate_type: Any = None
    aggregate_config: List[str] = field(default_factory=list)


@dataclass
class AutoCollectRemoveConfigCls(object):
    type: str
    unit: str
    index: int
    active: bool = False
    is_err: bool = False
    value: Any = None


@dataclass
class AutoCollectConfigCls(object):
    remove_config: List[AutoCollectRemoveConfigCls]
    auto_remove: bool = False
    auto_append: bool = True


@dataclass
class AutoCollectCls(object):
    """
    创建或者更新自动修改样本集配置
    """

    result_table_id: str
    sample_set_id: int
    project_id: int
    config: AutoCollectConfigCls
    apply_type: Any = None


@dataclass
class CommitApplyCls(object):
    """
    执行样本集提交
    """

    sample_set_id: int
    project_id: int


@dataclass
class SubmitStatusCls(object):
    """
    查询提交后的执行状态
    """

    project_id: int


@dataclass
class DeleteSampleSet(object):
    """
    删除样本集
    """

    project_id: int
