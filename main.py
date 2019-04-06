from pprint import pprint
# Install Pyaml
import yaml


# A default main function
def main():

    # Read and parse our yaml configuration
    with open('config.yaml', 'r') as yaml_file:
        configObject = yaml.load(yaml_file)
        pprint(configObject)


if __name__ == '__main__':
    main()
