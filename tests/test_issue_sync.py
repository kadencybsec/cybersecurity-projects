"""Run locally with: python3 -m unittest discover -s tests -v"""
import unittest
from scripts.sync_issue_progress import extract_steps, synchronize

class ProgressSyncTests(unittest.TestCase):
    def setUp(self):
        self.register = {"projects":[{"id":"B06","steps":[
            {"id":f"B06-S{i}","status":"not_started","evidence":[]}
            for i in range(1,5)
        ]}]}

    def issue(self, checks):
        body = "\n".join(
            f"- [{'x' if x else ' '}] **B06-S{i}** Task {i}"
            for i,x in enumerate(checks,1)
        )
        return {"title":"B06 · Home cybersecurity lab", "body":body}

    def test_started_tasks_do_not_count(self):
        self.assertFalse(synchronize(self.register, self.issue([False]*4)))
        self.assertTrue(all(x["status"]=="not_started" for x in self.register["projects"][0]["steps"]))

    def test_only_checked_steps_are_completed(self):
        self.assertTrue(synchronize(self.register,self.issue([True,False,False,False])))
        self.assertEqual("completed",self.register["projects"][0]["steps"][0]["status"])
        self.assertEqual("not_started",self.register["projects"][0]["steps"][1]["status"])

    def test_in_progress_is_preserved(self):
        self.register["projects"][0]["steps"][0]["status"]="in_progress"
        self.assertFalse(synchronize(self.register,self.issue([False]*4)))
        self.assertEqual("in_progress",self.register["projects"][0]["steps"][0]["status"])

    def test_uncheck_reopens_only_checked_task(self):
        self.register["projects"][0]["steps"][0]["status"]="completed"
        self.assertTrue(synchronize(self.register,self.issue([False]*4)))
        self.assertEqual("not_started",self.register["projects"][0]["steps"][0]["status"])

    def test_unrelated_issue_is_ignored(self):
        self.assertFalse(synchronize(self.register, {"title":"Help wanted", "body":"- [x] unrelated"}))

if __name__=="__main__":
    unittest.main()
