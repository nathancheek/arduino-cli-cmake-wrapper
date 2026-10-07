"""Test ``arduino_cli_cmake_wrapper.miner`` core archive detection."""

from pathlib import Path

from arduino_cli_cmake_wrapper.miner import sketch_cache
from arduino_cli_cmake_wrapper.types import Stage


def test_sketch_cache_with_trailing_core_step():
    """Find core.a when another step follows the archive (newer esp32 cores)."""
    stages = {
        Stage.CORE: [
            'gcc -c core/main.cpp -o /cache/core/main.cpp.o',
            'gcc-ar cr /cache/core/core.a /cache/core/main.cpp.o',
            '/usr/bin/env bash -c ": > \'/cache/file_opts\'"',
        ]
    }
    assert sketch_cache(stages) == Path('/cache')
