from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from marker.config.parser import ConfigParser
import os

config = {"output_format": "json", "ADDITIONAL_KEY": "VALUE"}
config_parser = ConfigParser(config)

converter = PdfConverter(
    config=config_parser.generate_config_dict(),
    artifact_dict=create_model_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer(),
    llm_service=config_parser.get_llm_service(),
)
for fileName in os.listdir("./testXactimateData/"):
    rendered = converter(f"./testXactimateData/{fileName}")
    text, _, images = text_from_rendered(rendered)
    print(text)
    new_directory = "./convertedXactimateJsonFiles/"
    fileName = fileName[:-4]
    new_file = open(new_directory + f"Json{fileName}", "w")
    new_file.write(text)
    new_file.close()
