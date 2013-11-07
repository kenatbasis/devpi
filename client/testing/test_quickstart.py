import py
import subprocess

def test_dryrun(cmd_devpi):
    cmd_devpi("quickstart", "--dry-run")

def test_functional(cmd_devpi, monkeypatch, tmpdir):
    monkeypatch.setenv("DEVPI_SERVERDIR", tmpdir.join("server"))
    monkeypatch.setenv("DEVPI_CLIENTDIR", tmpdir.join("client"))
    cmd_devpi("quickstart")
    try:
        hub = cmd_devpi("quickstart")
        assert isinstance(hub.sysex, SystemExit)
    finally:
        p = py.path.local.sysfind("devpi-server")
        subprocess.check_call([str(p), "--stop"])
