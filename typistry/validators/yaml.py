import yaml
from returns.result import Result, Success, Failure

from typistry.protos.invalid_object import InvalidObject

from typistry.protos.typed_dict import TypedDict

def safe_parse_yaml(file: str) -> Result[TypedDict, InvalidObject]:
    try:
        with open(file, 'r') as stream:
            try:
                yaml_load = yaml.safe_load(stream)
                if isinstance(yaml_load, dict):
                    to_type = yaml_load.get("type")
                    if isinstance(to_type, str):
                        yaml_load.pop("type")
                        return Success(TypedDict(yaml_load, type=to_type))
                    else:
                        return Failure(InvalidObject("Invalid YAML {file}: {yaml_load}.  Parsed object must contain 'type'", file))
                else:
                    return Failure(InvalidObject(f"\nInvalid YAML {file}: {yaml_load}.  Parsed object must be a dict", file))
            except yaml.YAMLError as exc:
                return Failure(InvalidObject(f"\nInvalid YAML {file}: {exc}\n", file))
    except FileNotFoundError as e:
        return Failure(InvalidObject(f"Specified YAML does not exist: {e}", file))

