"""The VietFin Standardized Data Model."""

from pydantic import BaseModel, ConfigDict, model_validator


class Data(BaseModel):
    """The VietFin Standardized Data Model.

    source: https://github.com/OpenBB-finance/OpenBBTerminal/blob/develop/openbb_platform/core/openbb_core/provider/abstract/data.py

    The `Data` class is a flexible Pydantic model designed to accommodate various data structures
    for VietFin's data processing pipeline as it's structured to support dynamic field definitions.

    Attributes
    ----------
    __alias_dict__ : dict[str, str]
        A dictionary that maps field names to their aliases,
        facilitating the use of different naming conventions.
    model_config : ConfigDict
        A configuration dictionary that defines the model's behavior,
        such as accepting extra fields, populating by name, and alias
        generation.

    """

    __alias_dict__: dict[str, str] = {}

    model_config = ConfigDict(
        extra="ignore",
        populate_by_name=True,
        strict=False,
    )

    # Transform a dictionary of values received from external input,
    # to match the internal naming conventions of the Pydantic model
    # This method is invoked before the inner validator of the Pydantic model is called
    @model_validator(mode="before")
    @classmethod
    def _use_alias(cls, values) -> dict:
        """Maps field names to their aliases."""
        # swapping the keys and values of __alias_dict__
        aliases = {
            alias: original for original, alias in cls.__alias_dict__.items()
        }
        if aliases:
            return {
                aliases.get(key, key): value for key, value in values.items()
            }
        return values
