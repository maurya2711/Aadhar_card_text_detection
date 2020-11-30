{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['删H或EK部可', 'GovernmentofIndia', '者存者标', 'Vaibhav Chaudhamy', '信倍00B:28/011998', '/MALE', '460899373037', 'LLL3Ln634na5荜505', '了T3T电TTT,可TT记TT']\n"
     ]
    }
   ],
   "source": [
    "text_output=open(\"./test_result/bro.txt\",\"r\")\n",
    "\n",
    "res=[]\n",
    "for line in text_output:\n",
    "    \n",
    "    res.append(line[:-1])\n",
    "    \n",
    "res[4]=res[4][6:]\n",
    "res[5]=res[5][1:]\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Vaibhav Chaudhamy', 'DOB': '28/011998', 'Gender': 'MALE', 'AADHAR NUMBER': '460899373037'}\n"
     ]
    }
   ],
   "source": [
    "final={\"Name\":result[3],\n",
    "      \"DOB\":result[4],\n",
    "      \"Gender\":result[5],\n",
    "      \"AADHAR NUMBER\":result[6]}\n",
    "\n",
    "print(final)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "\n",
    "with open (\"result.json\",\"w\") as output:\n",
    "    json.dump(final,output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
