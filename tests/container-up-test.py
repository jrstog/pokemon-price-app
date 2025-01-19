import unittest
import docker

class TestDockerContainer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Initialize Docker Client
        cls.client = docker.from_env()

    def test_container_output(self):
        #Expected output
        expected = "Congratulations, your container has started!"

        #Build Docker Image
        image, build_logs = self.client.images.build(path=".", tag="pokemon-price-app")

        #Run Container
        container = self.client.containers.run(
            "pokemon-price-app",
            detach=True,
            stdout=True,
            stderr=True
        )

        #Wait for Container to Start
        container.wait()

        #Capture Container Output
        output = container.logs().decode('utf-8')

        print("Expected Output: " + expected)
        print("Actual Output: " + output)

        #Compare Container Output to Expected
        self.assertIn(expected, output)

        #Stop and remove container
        container.remove()

if __name__ == "__main__":
    unittest.main()