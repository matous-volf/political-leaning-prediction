use serde::{Deserialize, Serialize};

#[derive(PartialEq, Serialize, Deserialize, Clone, Debug)]
pub enum Politicalness {
    Nonpolitical,
    Political,
}

impl TryFrom<&str> for Politicalness {
    type Error = ();

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        match value {
            "non-political" => Ok(Self::Nonpolitical),
            "political" => Ok(Self::Political),
            _ => Err(()),
        }
    }
}
