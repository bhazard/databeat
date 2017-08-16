from databeat import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Databeat normally
        """
        self.render_config_template(
            path=os.path.abspath(self.working_dir) + "/log/*"
        )

        databeat_proc = self.start_beat()
        self.wait_until(lambda: self.log_contains("databeat is running"))
        exit_code = databeat_proc.kill_and_wait()
        assert exit_code == 0
