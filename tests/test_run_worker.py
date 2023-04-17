import uuid

import pytest

from temporalio import activity
from temporalio.worker import Worker
from temporalio.testing import WorkflowEnvironment

from activities import get_bowl, put_bowl_away, add_cereal, put_cereal_back_in_box, add_milk
from workflows import BreakfastWorkflow

@pytest.mark.asyncio
async def test_execute_workflow():
    task_queue_name = str(uuid.uuid4())
    async with await WorkflowEnvironment.start_time_skipping() as env:

        async with Worker(
            env.client,
            task_queue=task_queue_name,
            workflows=[BreakfastWorkflow],
            activities=[get_bowl, put_bowl_away, add_cereal, put_cereal_back_in_box, add_milk],
        ):
            await env.client.execute_workflow(
                BreakfastWorkflow.run,
                "World",
                id=str(uuid.uuid4()),
                task_queue=task_queue_name,
            )


@activity.defn(name="say_hello")
async def say_hello_mocked(name: str) -> str:
    return f"Hello, {name} from mocked activity!"


@pytest.mark.asyncio
async def test_mock_activity():
    task_queue_name = str(uuid.uuid4())
    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with Worker(
            env.client,
            task_queue=task_queue_name,
            workflows=[BreakfastWorkflow],
            activities=[say_hello_mocked],
        ):
            assert "Hello, World from mocked activity!" == await env.client.execute_workflow(
                BreakfastWorkflow.run,
                "World",
                id=str(uuid.uuid4()),
                task_queue=task_queue_name,
            )
