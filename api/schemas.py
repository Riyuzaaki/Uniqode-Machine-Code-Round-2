from pydantic import BaseModel, Field, model_validator
from typing import Optional
import os
from api.config import PlanTiers, PostCategory

class Detect(BaseModel):
    """
    Pydantic model for detection requests.
    """
    text: str = Field(..., min_length=1, description="Text data for detection")
    final_score: Optional[int] = Field(default=None, description="Final score for the detection")
    

class CreatePostRequestData(BaseModel):
    description: str
    plans : PlanTiers
    category : PostCategory
    
class CreatePostResponse(BaseModel):
    post_id : int 

