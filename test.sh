#!/bin/bash

source .env
echo ""
echo "==================="
echo "Running Unit Tests"
echo "==================="

pytest player_session_service/tests/core

echo ""
echo "==================="
echo "   Testing API"
echo "==================="

tavern-ci --stdout player_session_service/tests/apis/player_events.tavern.yaml
