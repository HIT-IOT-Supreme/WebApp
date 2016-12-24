#!/usr/bin/env bash
mkdir log
supervisord -c supervisor.conf
supervisorctl -c supervisor.conf status