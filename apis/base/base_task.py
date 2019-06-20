from celery import Task


class BaseTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print("*"*50)
        print('task done: {0}'.format(retval))
        print('task_id is : {0}'.format(task_id))
        print("*" * 50)
        return super(BaseTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        print('task_id is : {0}'.format(task_id))
        return super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)
