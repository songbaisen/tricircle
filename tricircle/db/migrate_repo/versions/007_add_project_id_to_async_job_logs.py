# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table


def upgrade(migrate_engine):
    """Function adds project_id field."""
    meta = MetaData(bind=migrate_engine)

    # Add a new column project_id for async_job_logs
    async_job_logs = Table('async_job_logs', meta, autoload=True)
    project_id = Column('project_id', String(36), nullable=True)

    if not hasattr(async_job_logs.c, 'project_id'):
        async_job_logs.create_column(project_id)
