"""
Pipeline Entry Point.

Author: Simba Munatsi
"""

from src.pipeline.orchestrator import PipelineOrchestrator


def main():

    pipeline = PipelineOrchestrator()

    pipeline.run()


if __name__ == "__main__":

    main()